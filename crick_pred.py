import streamlit as st
import pickle
import numpy as np
import pandas as pd

def load_model():
    with open('pickle files/cricket_pred.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def load_batting_pred():
    with open('pickle files/batsman_score.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

def load_bowling_pred():
    with open('pickle files/bowler_wickets.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


#For score prediction
data = load_model()
dec_tree_reg = data['model']
le_venue = data['le_venue']
le_pitch_cond = data['le_pitch_cond']
le_batting_team = data['le_batting_team']
le_bowling_team = data['le_bowling_team']


#For batting prediction
batting_pred = load_batting_pred()
bat_pred_model = batting_pred['model']
le_score_venue = batting_pred['le_score_venue']
le_score_pitchcond = batting_pred['le_score_pitchcond']
le_score_bat = batting_pred['le_score_bat']
le_score_bowl = batting_pred['le_score_bowl']
le_score_striker = batting_pred['le_score_striker']


#For bowling prediction
bowling_pred = load_bowling_pred()
bowl_pred_model = bowling_pred['model']
le_wick_venue = bowling_pred['le_wick_venue']
le_wick_pitchcond = bowling_pred['le_wick_pitchcond']
le_wick_bat = bowling_pred['le_wick_bat']
le_wick_bowl = bowling_pred['le_wick_bowl']
le_wick_bowler = bowling_pred['le_wick_bowler']


def filter_results(data):
    d_temp = data
    data = {}
    for i in range(7):
        maxKey = max(d_temp, key=d_temp.get)
        data[maxKey] = d_temp[maxKey]
        d_temp.pop(maxKey)
    return data
    

def show_predict_page():
    bat_results = {}
    bowl_results = {}
    
    st.title("Cricket Team Prediction")
    st.write("""### We need some information for prediction""")

    venues = ('Tolerance Oval',
       'Rajiv Gandhi International Cricket Stadium, Dehradun',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'M.Chinnaswamy Stadium', 'Bready Cricket Club, Magheramason',
       'Bready', 'ICC Academy',
       'Al Amerat Cricket Ground Oman Cricket (Ministry Turf 1)',
       'Amini Park', 'Sportpark Maarschalkerweerd',
       'Takashinga Sports Club', 'Adelaide Oval',
       'Brisbane Cricket Ground, Woolloongabba',
       'Melbourne Cricket Ground', 'Sydney Cricket Ground', 'Manuka Oval',
       'Perth Stadium', 'Junction Oval', 'Kyambogo Cricket Oval',
       'Lugogo Cricket Oval', 'King George V Sports Ground',
       'College Field', 'Buffalo Park', 'Kingsmead', 'SuperSport Park',
       'The Wanderers Stadium', "St George's Park", 'Newlands',
       'Kinrara Academy Oval',
       'Punjab Cricket Association IS Bindra Stadium, Mohali',
       'Arun Jaitley Stadium', 'Saurashtra Cricket Association Stadium',
       'Vidarbha Cricket Association Stadium, Jamtha',
       'Rajiv Gandhi International Stadium, Uppal',
       'Greenfield International Stadium', 'Wankhede Stadium',
       'Hagley Oval', 'Westpac Stadium', 'Saxton Oval', 'McLean Park',
       'Eden Park', 'Seddon Park', 'Bay Oval', 'Basin Reserve',
       'Hazelaarweg', 'Central Broward Regional Park Stadium Turf Ground',
       'Providence Stadium, Guyana', 'Indian Association Ground',
       'VRA Ground', 'Sportpark Westvliet',
       'Pallekele International Cricket Stadium',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium',
       'Shere Bangla National Stadium, Mirpur',
       'Zahur Ahmed Chowdhury Stadium', 'White Hill Field, Sandys Parish',
       'National Stadium', 'Bermuda National Stadium',
       'United Cricket Club Ground', 'The Rose Bowl', 'Old Trafford',
       'Gaddafi Stadium', 'Sheikh Zayed Stadium',
       'ICC Academy Ground No 2', 'Dubai International Cricket Stadium',
       'The Village, Malahide', 'La Manga Club Bottom Ground',
       'Holkar Cricket Stadium',
       'Maharashtra Cricket Association Stadium',
       'National Cricket Stadium, Grenada', 'Warner Park, St Kitts',
       'Desert Springs Cricket Ground',
       'Tribhuvan University International Cricket Ground',
       'Al Amerat Cricket Ground Oman Cricket (Ministry Turf 2)',
       'Greater Noida Sports Complex Ground', 'Terdthai Cricket Ground',
       'Pierre Werner Cricket Ground', 'Rawalpindi Cricket Stadium',
       'University Oval', 'Sky Stadium', 'Moara Vlasiei Cricket Ground',
       'Boland Park', 'Trent Bridge, Nottingham', 'Headingley, Leeds',
       'Old Trafford, Manchester', 'Narendra Modi Stadium',
       'Sophia Gardens, Cardiff', 'The Rose Bowl, Southampton',
       'The Wanderers Stadium, Johannesburg',
       'SuperSport Park, Centurion', 'The Village, Malahide, Dublin',
       'Civil Service Cricket Club, Stormont, Belfast',
       'Coolidge Cricket Ground, Antigua',
       'Kensington Oval, Bridgetown, Barbados', 'Harare Sports Club',
       'Wanderers', 'Wanderers Cricket Ground, Windhoek',
       'Tribhuvan University International Cricket Ground, Kirtipur',
       'R Premadasa Stadium, Colombo',
       "National Cricket Stadium, St George's, Grenada",
       'Daren Sammy National Cricket Stadium, Gros Islet, St Lucia',
       'Manuka Oval, Canberra', 'Scott Page Field, Vinor',
       'National Sports Academy, Sofia', 'Marsa Sports Club',
       'Bayer Uerdingen Cricket Ground', 'Castle Avenue, Dublin',
       'Bready Cricket Club, Magheramason, Bready',
       'Svanholm Park, Brondby', 'Gucherre Cricket Ground',
       'Gahanga International Cricket Stadium. Rwanda',
       'Kerava National Cricket Ground',
       'Grange Cricket Club Ground, Raeburn Place, Edinburgh',
       'Zayed Cricket Stadium, Abu Dhabi', 'Sharjah Cricket Stadium',
       'Entebbe Cricket Oval', 'Desert Springs Cricket Ground, Almeria',
       'Moara Vlasiei Cricket Ground, Ilfov County',
       'Sawai Mansingh Stadium, Jaipur',
       'JSCA International Stadium Complex, Ranchi',
       'Eden Gardens, Kolkata',
       'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
       'Himachal Pradesh Cricket Association Stadium, Dharamsala',
       'Happy Valley Ground', 'ICC Academy, Dubai',
       'Integrated Polytechnic Regional Centre',
       'University of Lagos Cricket Oval',
       'West End Park International Cricket Stadium, Doha',
       'Sir Vivian Richards Stadium, North Sound, Antigua',
       'National Stadium, Karachi', 'Gaddafi Stadium, Lahore',
       'Central Broward Regional Park Stadium Turf Ground, Lauderhill',
       'United Cricket Club Ground, Windhoek')

    #teams = ('United Arab Emirates', 'Australia', 'Ireland', 'Afghanistan',
       #'India', 'Zimbabwe', 'Nepal', 'Scotland', 'Netherlands', 'Oman',
       #'Papua New Guinea', 'Philippines', 'Vanuatu',
       #'United States of America', 'Germany', 'Italy', 'Namibia', 'Kenya',
       #'Sri Lanka', 'Pakistan', 'England', 'Ghana', 'Uganda', 'Botswana',
       #'Nigeria', 'Guernsey', 'Denmark', 'Norway', 'Jersey',
       #'South Africa', 'Thailand', 'Malaysia', 'Maldives', 'Bangladesh',
       #'West Indies', 'New Zealand', 'Singapore', 'Qatar', 'Kuwait',
       #'Bermuda', 'Canada', 'Cayman Islands', 'Hong Kong', 'Portugal',
       #'Spain', 'Gibraltar', 'Bhutan', 'Saudi Arabia', 'Bahrain', 'Iran',
       #'Belgium', 'Luxembourg', 'Czech Republic', 'Isle of Man',
       #'Bulgaria', 'Romania', 'Austria', 'Greece', 'Serbia', 'Malta',
       #'France', 'Sweden', 'Rwanda', 'Finland', 'Hungary', 'Estonia',
       #'Cyprus', 'Switzerland', 'Swaziland', 'Lesotho', 'Seychelles',
       #'Malawi', 'Sierra Leone', 'Tanzania', 'Mozambique', 'Cameroon',
       #'Belize', 'Bahamas', 'Argentina', 'Panama')
    
    teams = ('Australia', 'Ireland', 'Afghanistan', 'India', 'Zimbabwe', 
             'Scotland', 'Netherlands', 'Namibia', 'Kenya', 'Sri Lanka', 
             'Pakistan', 'England', 'South Africa', 'Bangladesh', 
             'West Indies', 'New Zealand', 'Bermuda')
    
    pitch_condition = ('batting', 'bowling')
    
    team_players = {'Australia': ['SA Abbott',
      'AJ Tye',
      'PSP Handscomb',
      'AJ Turner',
      'TM Head',
      'PJ Cummins',
      'MC Henriques',
      'AC Agar',
      'JP Behrendorff',
      'A Zampa',
      'DA Warner',
      'GJ Maxwell',
      'AJ Finch',
      'MS Wade',
      'AT Carey',
      'DT Christian',
      'JR Hazlewood',
      'B Stanlake',
      'MR Marsh',
      'MA Starc',
      'JA Richardson',
      'DJM Short',
      'BR McDermott',
      'KW Richardson',
      'MJ Swepson',
      'MP Stoinis',
      'CA Lynn',
      'SPD Smith'],
    
     'Ireland': ['PR Stirling',
      'WB Rankin',
      'AR McBrine',
      'HT Tector',
      'GJ Thompson',
      'GH Dockrell',
      'GC Wilson',
      'Simi Singh',
      'MR Adair',
      'SW Poynter',
      'GJ Delany',
      'BJ McCarthy',
      'PKD Chase',
      'DC Delany',
      'SR Thompson',
      'SC Getkate',
      'CA Young',
      'TE Kane',
      'A Balbirnie',
      "KJ O'Brien"],
    
     'Afghanistan': ['Fazal Niazai',
      'Hamid Hassan',
      'Karim Janat',
      'Fareed Ahmad',
      'Amir Hamza',
      'Shapoor Zadran',
      'Mohammad Shahzad',
      'Usman Ghani',
      'Sayed Shirzad',
      'Najeeb Tarakai',
      'Dawlat Zadran',
      'Mujeeb Ur Rahman',
      'Najibullah Zadran',
      'Gulbadin Naib',
      'Qais Ahmad',
      'Shafiqullah',
      'Rahmanullah Gurbaz',
      'Sharafuddin Ashraf',
      'Mohammad Nabi',
      'Ibrahim Zadran',
      'Rashid Khan'],
    
     'India': ['MS Dhoni',
      'KD Karthik',
      'UT Yadav',
      'DL Chahar',
      'KH Pandya',
      'HH Pandya',
      'Mohammed Shami',
      'SS Iyer',
      'KK Ahmed',
      'RG Sharma',
      'S Dhawan',
      'NA Saini',
      'Kuldeep Yadav',
      'RD Chahar',
      'R Ashwin',
      'MK Pandey',
      'M Markande',
      'JJ Bumrah',
      'Mohammed Siraj',
      'YS Chahal',
      'RA Jadeja',
      'KL Rahul',
      'Washington Sundar',
      'SN Thakur',
      'B Kumar',
      'S Kaul',
      'S Dube',
      'AR Patel',
      'RR Pant'],
    
     'Zimbabwe': ['CR Ervine',
      'T Maruma',
      'SC Williams',
      'TS Chisoro',
      'TL Chatara',
      'N Madziva',
      'DT Tiripano',
      'BRM Taylor',
      'CB Mpofu',
      'TS Kamunhukamwe',
      'CK Tshuma',
      'R Mutumbami',
      'H Masakadza',
      'A Ndlovu',
      'PJ Moor',
      'KM Jarvis',
      'B Muzarabani',
      'CT Mutombodzi',
      'Sikandar Raza',
      'TK Musakanda',
      'LM Jongwe',
      'RW Chakabva',
      'SF Mire',
      'T Munyonga',
      'BB Chari',
      'B Mavuta',
      'E Chigumbura',
      'RP Burl',
      'WT Mashinge',
      'W Madhevere',
      'R Ngarava',
      'CT Mumba',
      'CJ Chibhabha',
      'D Jakiel',
      'WP Masakadza'],
    
     'Scotland': ['MA Leask',
      'Hamza Tahir',
      'JH Davey',
      'MH Cross',
      'HG Munsey',
      'SM Sharif',
      'CB Sole',
      'MRJ Watt',
      'KJ Coetzer',
      'CS MacLeod',
      'OJ Hairs',
      'CD Wallace',
      'RAJ Smith',
      'BTJ Wheal',
      'AC Evans',
      'DE Budge',
      'TB Sole',
      'A Neill',
      'GT Main',
      'RD Berrington'],
    
     'Netherlands': ['SA Edwards',
      'W Barresi',
      'TP Visee',
      'Sikander Zulfiqar',
      'PM Seelaar',
      'PA van Meekeren',
      'SJ Myburgh',
      'BN Cooper',
      'HC Overdijk',
      'VJ Kingma',
      "MP O'Dowd",
      'RN ten Doeschate',
      'Vikramjit Singh',
      'RE van der Merwe',
      'BD Glover',
      'TS Braat',
      'T van der Gugten',
      'S Snater',
      'BFW de Leede',
      'AJ Staal',
      'CN Ackermann',
      'PRP Boissevain',
      'C Floyd',
      'Saqib Zulfiqar',
      'FJ Klaassen'],
    
     'Namibia': ['JN Frylinck',
      'C Viljoen',
      'HN Ya France',
      'T Lungameni',
      'BM Scholtz',
      'N Davin',
      'B Shikongo',
      'CG Williams',
      'L Louwrens',
      'MG Erasmus',
      'D Wiese',
      'ZE Green',
      'SJ Baard',
      'JJ Smit',
      'K Birkenstock',
      'Z Groenewald',
      'JP Kotze'],
    
     'Kenya': ['E Ochieng',
      'IA Karim',
      'LN Oluoch',
      'RN Patel',
      'RR Patel',
      'SR Bhudia',
      'E Otieno',
      'AR Gandhi',
      'AA Obanda',
      'NN Odhiambo',
      'JS Kundi',
      'DM Gondaria',
      'EB Ringera',
      'NM Odhiambo',
      'P Kerai',
      'CO Obuya',
      'SO Ngoche'],
    
     'Sri Lanka': ['BKG Mendis',
      'I Udana',
      'SL Malinga',
      'AK Perera',
      'MD Gunathilaka',
      'N Dickwella',
      'MDKJ Perera',
      'N Pradeep',
      'LD Madushanka',
      'B Fernando',
      'MD Shanaka',
      'CAK Rajitha',
      'S Samarawickrama',
      'WIA Fernando',
      'BOP Fernando',
      'AD Mathews',
      'GSNFG Jayasuriya',
      'NLTC Perera',
      'PBB Rajapaksa',
      'M Bhanuka',
      'CBRLS Kumara',
      'PVD Chameera',
      'PWH de Silva',
      'JDF Vandersay',
      'DM de Silva',
      'A Dananjaya',
      'LD Chandimal',
      'PHKD Mendis',
      'PADLR Sandakan'],
    
     'Pakistan': ['Ahmed Shehzad',
      'Mohammad Amir',
      'Wahab Riaz',
      'Umar Akmal',
      'Haris Rauf',
      'Babar Azam',
      'Khushdil Shah',
      'Muhammad Musa',
      'Ahsan Ali',
      'Iftikhar Ahmed',
      'Sohaib Maqsood',
      'Faheem Ashraf',
      'Haris Sohail',
      'Mohammad Hafeez',
      'Shoaib Malik',
      'Mohammad Hasnain',
      'Mohammad Rizwan',
      'Mohammad Nawaz (3)',
      'Usman Shinwari',
      'Hussain Talat',
      'Fakhar Zaman',
      'Shadab Khan',
      'Imad Wasim',
      'Hasan Ali',
      'Mohammad Irfan',
      'Sharjeel Khan',
      'Asif Ali',
      'Shaheen Shah Afridi'],
    
     'England': ['S Mahmood',
      'TS Mills',
      'AU Rashid',
      'DJ Malan',
      'JL Denly',
      'LS Livingstone',
      'MA Wood',
      'SM Curran',
      'CJ Jordan',
      'DJ Willey',
      'CR Woakes',
      'JJ Roy',
      'RJW Topley',
      'PR Brown',
      'SW Billings',
      'JC Archer',
      'T Banton',
      'JC Buttler',
      'LA Dawson',
      'MM Ali',
      'JM Vince',
      'MW Parkinson',
      'JM Bairstow',
      'TK Curran',
      'EJG Morgan',
      'L Gregory',
      'BA Stokes'],
    
     'South Africa': ['CJ Dala',
      'L Ngidi',
      'DW Steyn',
      'AK Markram',
      'JN Malan',
      'Q de Kock',
      'F du Plessis',
      'A Nortje',
      'AL Phehlukwayo',
      'PJ van Biljon',
      'L Sipamla',
      'RR Hendricks',
      'DA Miller',
      'JT Smuts',
      'T Bavuma',
      'H Klaasen',
      'D Pretorius',
      'BE Hendricks',
      'K Rabada',
      'HE van der Dussen',
      'T Shamsi',
      'BC Fortuin'],
    
     'Bangladesh': ['Taijul Islam',
      'Tamim Iqbal',
      'Taskin Ahmed',
      'Mahedi Hasan',
      'Mohammad Mithun',
      'Mosaddek Hossain',
      'Rubel Hossain',
      'Afif Hossain',
      'Mohammad Naim',
      'Shakib Al Hasan',
      'Mohammad Saifuddin',
      'Soumya Sarkar',
      'Sabbir Rahman',
      'Mustafizur Rahman',
      'Hasan Mahmud',
      'Shafiul Islam',
      'Liton Das',
      'Mahmudullah',
      'Nurul Hasan',
      'Mushfiqur Rahim'],
    
     'West Indies': ['SD Hope',
      'JD Campbell',
      'LMP Simmons',
      'N Pooran',
      'HR Walsh',
      'KA Pollard',
      'DM Bravo',
      'ADS Fletcher',
      'FH Edwards',
      'O Thomas',
      'K Pierre',
      'JO Holder',
      'KOK Williams',
      'CH Gayle',
      'R Rampaul',
      'R Powell',
      'CR Brathwaite',
      'BA King',
      'OC McCoy',
      'D Ramdin',
      'DJ Bravo',
      'DC Thomas',
      'AD Russell',
      'FA Allen',
      'E Lewis',
      'SS Cottrell',
      'KMA Paul',
      'SE Rutherford',
      'SO Hetmyer',
      'R Shepherd',
      'OF Smith',
      'SP Narine'],
    
     'New Zealand': ['C de Grandhomme',
      'JDS Neesham',
      'MS Chapman',
      'TC Bruce',
      'KS Williamson',
      'TL Seifert',
      'MJ Guptill',
      'LH Ferguson',
      'HD Rutherford',
      'LRPL Taylor',
      'TA Boult',
      'TWM Latham',
      'TA Blundell',
      'DJ Mitchell',
      'DAJ Bracewell',
      'AF Milne',
      'HK Bennett',
      'IS Sodhi',
      'MJ Santner',
      'HM Nicholls',
      'SHA Rance',
      'C Munro',
      'GD Phillips',
      'TG Southee',
      'AY Patel',
      'TD Astle',
      'SC Kuggeleijn',
      'BM Tickner'],
    
     'Bermuda': ['OO Bascome',
      'DC Stovell',
      'O Bascome',
      'TS Fray',
      'RJ Trott',
      'DL Brangman',
      "GH O'Brien",
      'MO Jones',
      'KC Hodsoll',
      'M Simmons',
      'S Smith',
      'OGL Bascome',
      'DAP Darrell',
      'JE Pitcher',
      'AC Douglas',
      'KS Leverock',
      'JJ Tucker',
      'DMW Rawlins']}

    venue = st.selectbox("Venue", venues)
    team1 = st.selectbox("Team 1", teams)
    team2  = st.selectbox('Team 2', teams)
    pc = st.selectbox("Pitch Condition", pitch_condition) 

    predict = st.button("Start Prediction")
    if predict and (team1 != team2):
        X  = np.array([[venue, pc, team1, team2]])
        X[:,0] = le_venue.transform(X[:,0])
        X[:,1] = le_pitch_cond.transform(X[:,1])
        X[:,2] = le_batting_team.transform(X[:,2])
        X[:,3] = le_bowling_team.transform(X[:,3])
    
        score = dec_tree_reg.predict(X)
        st.subheader(f'The expected score  : {int(score[0])}')
     
            
        
        for i in team_players[team1]:
            try:
                bat_pred = np.array([[venue, pc, team1, team2, i]])
                bat_pred[:,0] = le_score_venue.transform(bat_pred[:,0])
                bat_pred[:,1] = le_score_pitchcond.transform(bat_pred[:,1])
                bat_pred[:,2] = le_score_bat.transform(bat_pred[:,2])
                bat_pred[:,3] = le_score_bowl.transform(bat_pred[:,3])
                bat_pred[:,4] = le_score_striker.transform(bat_pred[:,4])
            
                indi_rating = bat_pred_model.predict(bat_pred)
                bat_results[i] = int(indi_rating[0])
            except:
                continue
        
        
        for i in team_players[team1]:
            try:
                bowl_pred = np.array([[venue, pc, team1, team2, i]])
                bowl_pred[:,0] = le_wick_venue.transform(bowl_pred[:,0])
                bowl_pred[:,1] = le_wick_pitchcond.transform(bowl_pred[:,1])
                bowl_pred[:,2] = le_wick_bat.transform(bowl_pred[:,2])
                bowl_pred[:,3] = le_wick_bowl.transform(bowl_pred[:,3])
                bowl_pred[:,4] = le_wick_bowler.transform(bowl_pred[:,4])
                
                indi_wick = bowl_pred_model.predict(bowl_pred)
                bowl_results[i] = int(indi_wick[0])
            except:
                continue
            
        bat_results = filter_results(bat_results)
        bowl_results = filter_results(bowl_results)
        
        st.write("""## -------------------------------------------------------------""")
        st.write("""### Batting""")
                
        bat_df = pd.DataFrame({
            'Player': [i for i in bat_results.keys()],
            'Rating': [bat_results[i] for i in bat_results.keys()]
            })
        st.table(bat_df)
       
        
        st.write("""## -------------------------------------------------------------""")
        st.write("""### Bowling""")
        
        bowl_df = pd.DataFrame({
            'Player': [i for i in bowl_results.keys()],
            'Rating': [bowl_results[i] for i in bowl_results.keys()]
            })
        st.table(bowl_df)       