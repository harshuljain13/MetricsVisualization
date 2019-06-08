from resource import db


class eod_hd(db.Model):
    '''
    model for eod_hd
    '''
    #__table_args__ = {'schema':'pint_own'}
    __tablename__ = 'eod_hd'
    __columnsmap__ = {'id': 'float', 'open': 'float', 'high':'float',
                      'low':'float','close':'float','volume':'float',
                      'dividend':'float','split':'float','adjopen':'float',
                      'adjhigh':'float', 'adjlow':'float', 'adjclose':'float',
                      'adjvolume':'float', 'date':'date'}
    id = db.Column('id', db.Integer(), primary_key=True)
    Open = db.Column('Open', db.Float())
    High = db.column('High', db.Float())
    Low = db.Column('Low', db.Float())
    Close = db.Column('Close', db.Float())
    Volume = db.Column('Volume', db.Float())
    Dividend = db.column('Dividend', db.Float())
    Split = db.Column('Split', db.Float())
    AdjOpen = db.Column('AdjOpen', db.Float())
    AdjHigh = db.Column('AdjHigh', db.Float())
    AdjLow = db.Column('AdjLow', db.Float())
    AdjClose = db.Column('AdjClose', db.Float())
    AdjVolume = db.Column('Adjvolume', db.Float())
    Date = db.Column('Date', db.Date())