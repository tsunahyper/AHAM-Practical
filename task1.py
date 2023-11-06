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
    
    #response format for investment fund
    def fund_res(self):
        return  f"""Fund ID: {self.fund_id}\n
                    Fund Name: {self.fund_name}\n
                    Fund Manager: {self.fund_manager}\n
                    Description: {self.description}\n
                    NAV: {self.nav}\n
                    Creation Date: {self.creation_date}\n
                    Performance: {self.performance}%
                """
