class Company:

    # Class attribute
    company_name = 'Google' # shared with all instances
    location = 'California'
    employees = 182502

    def info(self):
        print("This method belongs to instance")

    @classmethod
    def get_name(cls):
        print(Company.company_name, cls.location)

