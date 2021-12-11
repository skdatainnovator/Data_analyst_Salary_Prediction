import streamlit as st
import pickle
import pandas as pd

def load_model():
   with open('data_analyst_SP.pkl','rb') as file:
      data = pickle.load(file)
   return data

model = load_model()

def show_predict_page():
      
   st.title("Data Analyst Salary Prediction")

   st.write("""### We need some information to predict the salary""")

   analyst_type = ('General Data Analyst', 'Quality Data Analyst',
       'Reporting Data Analyst', 'Business Data Analyst',
       'Governance Data Analyst', 'Healthcare Data Analyst',
       'Research Data Analyst', 'Financial Data Analyst',
       'SQL Data Analyst', 'Manager', 'Marketing Data Analyst')

   #rating  = float(input())

   job_exp = ('intermediate', 'senior', 'junior')

   company_size = ('1 to 50','51 to 200', '201 to 500' , '501 to 1000','1001 to 5000',
       '5001 to 10000', '10000+' )
  

   type_of_ownership = ('Nonprofit Organization', 'Company - Private',
       'Subsidiary or Business Segment', 'Company - Public', 'Hospital',
       'Contract', 'Government','Other Organization',
       'College / University', 'School / School District',
       'Self-employed', 'Private Practice / Firm', 'Franchise')

    #industry = input()

   sector = ('Non-Profit', 'Health Care', 'Information Technology',
       'Arts, Entertainment & Recreation', 'Finance', 'Insurance',
       'Business Services', 'Restaurants, Bars & Food Services',
       'Media', 'Accounting & Legal', 'Real Estate', 'Government',
       'Retail', 'Consumer Services', 'Biotech & Pharmaceuticals',
       'Education', 'Construction, Repair & Maintenance',
       'Oil, Gas, Energy & Utilities', 'Manufacturing',
       'Aerospace & Defense', 'Telecommunications',
       'Transportation & Logistics', 'Mining & Metals',
       'Travel & Tourism')

   revenue = ('$100 to $500 million', '$2 to $5 billion',
       '$50 to $100 million', '$1 to $2 billion', '$5 to $10 billion',
       '$1 to $5 million', '$25 to $50 million', '$10+ billion',
       'Less than $1 million', '$10 to $25 million',
       '$500 million to $1 billion', '$5 to $10 million')
   state = (' NY', ' NJ', ' UT', ' CA', ' VA', ' FL', ' IL', ' TX', ' AZ',
       ' PA', ' DE', ' OH', ' NC', ' SC', ' IN', ' WA', ' GA', ' KS',
       ' CO')
   city = ('Mesa', 'El Segundo', 'San Francisco', 'Philadelphia', 'Denver',
       'Chesapeake', 'Woodland Hills', 'Little Ferry', 'Tempe', 'Houston',
       'Wayne', 'South San Francisco', 'Chicago', 'Palo Alto', 'New York',
       'Maywood', 'Kent', 'Fort Worth', 'Pearland', 'Dallas',
       'Los Angeles', 'Greenwood Village', 'Centennial', 'Chandler',
       'Brooklyn', 'Columbus', 'San Diego', 'Irving', 'Allegheny West',
       'Portsmouth', 'Austin', 'Summit', 'Hampton', 'City of Industry',
       'Mountain View', 'Oakland', 'Lehi', 'Inglewood', 'Norfolk',
       'Beverly Hills', 'San Antonio', 'Sunnyvale', 'Cupertino',
       'Charlotte', 'Foster City', 'Indianapolis', 'Seattle',
       'Long Beach', 'Plano', 'Salt Lake City', 'Downers Grove',
       'Redwood City', 'Allen', 'Glendale', 'Jersey City',
       'Franklin Lakes', 'Fort Mill', 'Wilmington', 'Phoenix', 'Issaquah',
       'Los Gatos', 'Round Rock', 'San Jose', 'Menlo Park',
       'Mount Vernon', 'Florham Park', 'Broomfield', 'Hilliard',
       'San Mateo', 'Malvern', 'Santa Monica', 'Newark', 'Jacksonville',
       'Burbank', 'Horsham', 'Santa Clara', 'Lake Success', 'Cerritos',
       'Redmond', 'Northridge', 'Elk Grove Village', 'Westlake',
       'Plymouth Meeting', 'Kirkland', 'Scottsdale', 'Athens', 'Stafford',
       'Richardson', 'Union City', 'Walnut Creek', 'Fort Eustis',
       'Alhambra', 'Englewood', 'Grapevine', 'Weehawken', 'Mooresville',
       'Huntersville', 'Milpitas', 'Alachua', 'Fort Washington','Burlingame', 'Itasca', 'Southlake', 'Lakewood', 'Sugar Land',
       'Fort Sam Houston', 'Woodridge', 'Marlton', 'Pico Rivera',
       'King of Prussia', 'Mount Laurel', 'Fremont', 'Boulder',
       'San Rafael', 'Lawrence', 'West Chester', 'Iselin', 'Novato',
       'Arlington', 'Woodbridge', 'Henderson', 'San Ramon', 'Culver City',
       'West Point', 'Whippany', 'Northfield', 'Exton', 'Parsippany',
       'Millbrae', 'Gainesville', 'Carmel', 'American Fork',
       'Ridley Park', 'Addison', 'Hercules', 'Arcadia', 'Montvale',
       'Emeryville', 'Pleasanton', 'Queens Village', 'Pasadena', 'Aurora',
       'Boothwyn', 'El Cajon', 'Northbrook', 'Lackland AFB', 'Stanford',
       'Oak Brook', 'West Jordan', 'Berwyn', 'Radnor', 'Hanford',
       'DC Ranch', 'West Orange', 'Tarrant', 'Irwindale',
       'West Conshohocken', 'Glenview', 'South Plainfield',
       'East Palo Alto', 'Feasterville Trevose', 'Northlake',
       'Virginia Beach', 'Broadview', 'Essex Fells', 'Hoboken', 'Renton',
       'Venice', 'Littleton', 'Westerville', 'Berkeley', 'Topeka',
       'Burr Ridge', 'Hermosa Beach', 'Coppell', 'Beech Grove',
       'Smithfield', 'Evanston', 'Conshohocken', 'Secaucus', 'Anaheim',
       'Indian Trail', 'Haworth', 'Bridgeview', 'Farmers Branch',
       'Doylestown', 'Camden', 'Fort Lee', 'Moorestown',
       'Rolling Meadows', 'Bronx', 'Newtown Square', 'Suffolk', 'Reedley',
       'Dublin', 'Deerfield', 'Chester Township', 'Newport News',
       'Riverton', 'Daly City', 'Draper', 'Alameda', 'Campbell',
       'Long Island City', 'Marina del Rey', 'Brea', 'Roanoke', 'Paoli',
       'Visalia', 'Harrison')

    
    

    # input variable taken fron user for prediction
   Analyst_type = st.selectbox("Analyst Type", analyst_type)
   rating = 4
   Job_exp = st.selectbox("Enter your job experience",job_exp)
   Company_size = '5001 to 10000'
   Competitors_count = 4
   Company_age = int(st.slider("Company age",0,100,3))
   Type_of_ownership = 'Company - Private'
   Industry = st.text_input("Enter you Industry",'Information Technology')
   Sector = st.selectbox("Select your sector",sector)
   Revenue = st.selectbox("Select your company revenues",revenue)
   State = st.selectbox("Select your State",state)
   City = st.selectbox("Select Your City",city)

   language_used = st.multiselect("Select the Tools Used in you company",('SAS','Hadoop','Python','R','AWS','Azure','SQL','Excel','Machine Learning','Tableau','Power BI','Qlik'))

   ok = st.button("Predict Salary")

   if ok:
      if 'SAS' in language_used:
         SAS_extracted = 1
      else:
         SAS_extracted = 0

      if 'Hadoop' in language_used:
         Hadoop_extracted = 1
      else:
         Hadoop_extracted = 0

      if 'Python' in language_used:
         Python_extracted = 1
      else:
         Python_extracted = 0
      
      if 'R' in language_used:
         Rprogram_extracted = 1
      else:
         Rprogram_extracted = 0

      if 'AWS' in language_used:
         AWS_extracted = 1
      else:
         AWS_extracted = 0

      if 'Azure' in language_used:
         Azure_extracted = 1
      else:
         Azure_extracted = 0

      if 'SQL' in language_used:
         SQL_extracted = 1
      else:
         SQL_extracted = 0

      if 'Excel' in language_used:
         Excel_extracted = 1
      else:
         Excel_extracted = 0

      if 'Machine Learning' in language_used:
         MachineLearning_extracted = 1
      else:
         MachineLearning_extracted = 0

      if 'Tableau' in language_used:
         Tableau_extracted = 1
      else:
         Tableau_extracted = 0

      if 'Power BI' in language_used:
         PowerBI_extracted = 1
      else:
         PowerBI_extracted = 0
      
      if 'Qlik' in language_used:
         Qlik_extracted = 1
      else:
         Qlik_extracted = 0

   



      input_df = pd.DataFrame([[Analyst_type,rating,Job_exp,Company_size,Competitors_count,Company_age,Type_of_ownership,Industry,Sector,Revenue,State,City
        ,SAS_extracted,Hadoop_extracted,Python_extracted,Rprogram_extracted,AWS_extracted,Azure_extracted,SQL_extracted,
        Excel_extracted,MachineLearning_extracted,Tableau_extracted,PowerBI_extracted,Qlik_extracted]],columns=['Analyst_Type', 'Rating', 'Job_EXP', 'Size', 'Competitors_count',
       'Company_age', 'Type_of_ownership', 'Industry', 'Sector', 'Revenue',
       'State', 'City', 'SAS_extracted', 'Hadoop_extracted',
       'Python_extracted', 'R program_extracted', 'AWS_extracted',
       'Azure_extracted', 'SQL_extracted', 'Excel_extracted',
       'Machine Learning_extracted', 'Tableau_extracted', 'Power BI_extracted',
       'Qlik_extracted'])
      salary = int(model.predict(input_df))
      st.subheader(f"The Estimated Salary is ${salary}")

    

