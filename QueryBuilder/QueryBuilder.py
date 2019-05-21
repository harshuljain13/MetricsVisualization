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
        filter_query = self.construct_filter_query(query_dict['query_filters'])
        query_str = "select {0}({1}) from {2} where {3}".format(aggregation_type, columns, table_name, filter_query)
        return query_str
    
    def construct_filter_query(self, filters_dict):
        # recrusive algorithm to construct the filter query
        query_ = ''
        
        group_relation = filters_dict['relation']
        filters = filters_dict['filters']
        
        # iterate through every filter
        for i,filter_ in enumerate(filters):
            # make the query
            filter_type = filter_['filter_type']
            
            if filter_type == 'condition':
                operand = filter_['operand']
                operator = filter_['operator']
                value = filter_['value']
                filter_query = "{} {} {}".format(operand, operator, value)
                if i==0:
                    query_ += filter_query
                else:
                    query_ = "({} {} {})".format(query_, group_relation, filter_query)
            else:
                nest_query = self.construct_filter_query(filter_)
                if i==0:
                    query_ += "{}".format(nest_query)
                else:
                    query_ = "({} {} {})".format(query_, group_relation, nest_query)
                
        return query_
    
    