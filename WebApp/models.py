from resource import db

"""
class reliance(db.Model):
    '''
    model for reliance
    '''
    #__table_args__ = {'schema':'pint_own'}
    __tablename__ = 'reliance'
    __columnsmap__ = {'id': 'float', 'date': 'datetime', 'open_price': 'float', 'high_price':'float',
                      'low_price':'float','last_traded_price':'float','close_price':'float',
                      'total_traded_quantity':'float', 'turnover':'float'}
    id = db.Column('id', db.Integer(), primary_key=True)
    date = db.Column('date', db.Date())
    open_price = db.Column('open_price', db.Float())
    high_price = db.column('high_price', db.Float())
    low = db.Column('low_price', db.Float())
    last_traded_price = db.Column('last_traded_price', db.Float())
    close_price = db.Column('close_price', db.Float())
    total_traded_quantity = db.Column('total_traded_quantity', db.Float())
    turnover = db.column('turnover', db.Float())"""

class csv_data__csv_table(db.Model):
    __schema_name__ = 'csv_data'
    __tablename__ = 'csv_table'
    __columnsmap__ = {'id': 'integer', 'utilityname': 'string', 'statename': 'string', 'countyname':'string',
                      'outagecount':'integer','customercount':'integer','recorddatetime':'datetime',
                      'stepount':'integer', 'perdiff':'float', 'duration':'integer'}
    id = db.Column('id', db.Integer(), primary_key=True)
    utilityname = db.Column('utilitynamee', db.String())
    statename = db.Column('statename', db.String())
    countyname = db.column('countyname', db.String())
    outagecount = db.Column('outagecount', db.Integer())
    customercount = db.Column('customercount', db.Integer())
    recorddatetime = db.Column('recorddatetime', db.DateTime())
    stepcount = db.Column('stepcount', db.Integer())
    perdiff = db.column('perdiff', db.Float())
    duration = db.column('duration', db.Integer())
    