class investment_fund:
    #initialise investment fund requirements
    def __init__(self, fund_id, fund_name, fund_manager, description, nav, creation_date, performance):
        self.fund_id = fund_id
        self.fund_name = fund_name
        self.fund_manager = fund_manager
        self.description = description
        self.nav = nav
        self.creation_date = creation_date
        self.performance = performance