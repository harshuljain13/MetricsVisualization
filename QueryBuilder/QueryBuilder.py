'''
Core QueryBuilder Engine
'''

class QueryBuilder(object):
    '''
    Class defining the QueryBuilder behavior.
    '''
    def __init__(self, db_engine):
        # get the operator map for the specific db engine.
        pass
    
    def build_query_from_dict(self, query_dict):
        #parse the parameters from the json
        table_name = query_dict['table']
        columns = ','.join(query_dict['columns'])
        aggreation_col = query_dict['aggregation_columns']
        aggregation_type = query_dict['aggregation_type']
        filter_query = self.construct_filter_query(query_dict['filters'])
        query_str = "select {0}({1}) from {2} where {3}".format(aggregation_type, columns, table_name, filter_query)
        return query_str
    
    def construct_filter_query(self, filters):
        # recrusive algorithm to construct the filter query
        query_ = ''
        
        # iterate through every filter
        for i,filter_ in enumerate(filters):
            # make the query
            child_filters = filter_['child_filters']
            child_relation = filter_['child_relation']
            var = filter_['var']
            val = filter_['val']
            op = filter_['op']
            parent_relation = filter_['parent_relation']
            flt_query = "{}{}{}".format(var, op, val)

            if len(child_filters) ==0:
                if i==0:
                    query_ += flt_query
                else:
                    query_ = "({} {} {})".format(query_, parent_relation, flt_query)


            else:
                child_query = self.construct_filter_query(child_filters)
                flt_query = "({} {} {})".format(flt_query, child_relation, child_query)
                if i==0:
                    query_+=flt_query
                else:
                    query_ = "({} {} {})".format(query_, parent_relation, flt_query)
        return query_
    
    