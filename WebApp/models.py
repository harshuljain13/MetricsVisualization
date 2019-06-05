from resource import db


class snow_incidents_view(db.Model):
    '''
    model for pint_own.snow_incidents_view
    '''
    __table_args__ = {'schema':'pint_own'}
    __tablename__ = 'snow_incidents_view'
    __columnsmap__ = {'inc_id': 'String', 'inc_number': 'String', 'prb_id':'String',
                      'inc_caller':'String','inc_caller_dept':'String','inc_assignee':'String',
                      'inc_assignee_grp':'String','inc_labels':'String','inc_resolved_at':'datetime',
                      'inc_created_at':'datetime', 'inc_created_by':'String', 'inc_updated_at':'datetime',
                      'inc_business_impact':'String', 'inc_status':'String', 'inc_priority':'String',
                      'inc_env':'String', 'inc_summary':'String'}
    inc_id = db.Column('inc_id', db.String(32), primary_key=True)
    inc_number = db.Column('inc_number', db.String(10))
    prb_id = db.column('prb_id', db.String(32))
    inc_caller = db.Column('inc_caller', db.String(400))
    inc_caller_dept = db.Column('inc_caller_dept', db.String(400))
    inc_assignee = db.Column('inc_assignee', db.String(400))
    inc_assignee_grp = db.column('inc_assignee_grp', db.String(400))
    inc_labels = db.Column('inc_labels', db.String(4000))
    inc_resolved_at = db.Column('inc_resolved_at', db.DateTime())
    inc_created_at = db.Column('inc_created_at', db.DateTime())
    inc_created_by = db.Column('inc_created_by', db.String(100))
    inc_updated_at = db.Column('inc_updated_at', db.DateTime())
    inc_business_impact = db.Column('inc_business_impact', db.String(400))
    inc_status = db.Column('inc_status', db.String(20))
    inc_priority = db.Column('inc_priority', db.String(20))
    inc_env = db.Column('inc_env', db.String(20))
    inc_summary = db.Column('inc_summary', db.String(400))
    
    def __str__(self):
        return '({},{})'.format(self.inc_created_at, self.inc_number)
    
    def __repr__(self):
        return '({},{})'.format(self.inc_created_at, self.inc_number)
    
    
    
class snow_problems_view(db.Model):
    '''
    model for pint_own.snow_incidents_view
    '''
    __table_args__ = {'schema':'pint_own'}
    __tablename__ = 'snow_problems_view'
    __columnsmap__ = {'prb_id': 'String', 'prb_number': 'String', 
                      'prb_root_cause':'String','inc_caller_dept':'String','prb_assignee':'String',
                      'prb_assignee_grp':'String','prb_due_date':'String','prb_resolved_at':'datetime',
                      'prb_created_at':'datetime', 'prb_created_by':'String', 'prb_updated_at':'datetime',
                      'prb_business_impact':'String', 'prb_status':'String', 'prb_priority':'String',
                      'prb_summary':'String'}
    prb_id = db.Column('prb_id', db.String(32), primary_key=True)
    prb_number = db.Column('prb_number', db.String(10))
    prb_assignee = db.Column('prb_assignee', db.String(400))
    prb_assignee_grp = db.column('prb_assignee_grp', db.String(400))
    prb_resolved_at = db.Column('prb_resolved_at', db.DateTime())
    prb_created_at = db.Column('prb_created_at', db.DateTime())
    prb_created_by = db.Column('prb_created_by', db.String(100))
    prb_updated_at = db.Column('prb_updated_at', db.DateTime())
    prb_business_impact = db.Column('prb_business_impact', db.String(400))
    prb_status = db.Column('prb_status', db.String(20))
    prb_priority = db.Column('prb_priority', db.String(20))
    prb_root_cause = db.Column('prb_root_cause', db.String(100))
    prb_due_date = db.Column('prb_due_date', db.DateTime())
    prb_summary = db.Column('prb_summary', db.String(400))
    
    def __str__(self):
        return '({},{})'.format(self.prb_created_at, self.prb_number)
    
    def __repr__(self):
        return '({},{})'.format(self.prb_created_at, self.prb_number)