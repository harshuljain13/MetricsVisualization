from resource import db


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
    turnover = db.column('turnover', db.Float())
    