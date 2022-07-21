import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import pickle

def load_data():
    with open('pickle files/player_performance.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_data()

players_innings_batted = data['players_innings_batted']
batting_avg = data['batting_avg']
century_innings = data['century_innings']
fifty_innings = data['fifty_innings']
zeros_innings = data['zeros_innings']
highest_score = data['highest_score']
strike_rate_bat = data['strike_rate_bat']
players_innings_bowled = data['players_innings_bowled']
no_inn_bowled = data['no_inn_bowled']
bowling_avg = data['bowling_avg']
FF = data['FF']
strike_rate_bowl = data['strike_rate_bowl']
against_oppo_df = data['against_oppo_df']
consistency = data['consistency']


def extract_oppo(data, player):
    data = data[(data['player'] == player)]
    unique_oppo = data.Op.unique()
    
    player_data = []
   
    for i in unique_oppo:
        t_data = data.loc[(data['player'] == player) & (data['Op'] == i)].values.tolist()
        player_data.append(t_data[0])
    
    return player_data


def show_individual_stats():
    st.title("Individual Stats")
    st.write("""### Select player to see their stats""")
    
    
    players_list = ('Ibrahim Zadran','TA Blundell','MP Stoinis','VJ Kingma',
     'TS Kamunhukamwe',
     'DT Christian',
     'Mosaddek Hossain',
     'S Dube',
     'JL Denly',
     'Simi Singh',
     'LRPL Taylor',
     'RJW Topley',
     'BJ McCarthy',
     'CS MacLeod',
     'Hamid Hassan',
     'HG Munsey',
     'Usman Shinwari',
     'TB Sole',
     'BC Fortuin',
     'S Dhawan',
     'PJ Cummins',
     'HE van der Dussen',
     'T Munyonga',
     'Haris Sohail',
     'I Udana',
     'EB Ringera',
     'AJ Turner',
     'Rubel Hossain',
     'R Mutumbami',
     'PJ van Biljon',
     'JS Kundi',
     'D Jakiel',
     'Amir Hamza',
     'RR Patel',
     'SM Sharif',
     'MS Chapman',
     'HK Bennett',
     'PJ Moor',
     'TL Chatara',
     'JJ Bumrah',
     'Gulbadin Naib',
     'Taskin Ahmed',
     'M Markande',
     'B Muzarabani',
     'PKD Chase',
     'T Bavuma',
     'T Shamsi',
     'ADS Fletcher',
     'SR Bhudia',
     'B Mavuta',
     'DJ Willey',
     'AJ Tye',
     'SP Narine',
     "MP O'Dowd",
     'HR Walsh',
     'NLTC Perera',
     'CN Ackermann',
     'LD Madushanka',
     'Faheem Ashraf',
     'KA Pollard',
     'Hasan Mahmud',
     'JO Holder',
     'CA Lynn',
     'BD Glover',
     'NM Odhiambo',
     'Mohammad Hafeez',
     'Najibullah Zadran',
     'Soumya Sarkar',
     'WB Rankin',
     'KD Karthik',
     'LS Livingstone',
     'FH Edwards',
     'DL Chahar',
     'E Chigumbura',
     'AC Evans',
     'GJ Thompson',
     'BA Stokes',
     'DAP Darrell',
     'SA Abbott',
     'LD Chandimal',
     'RD Berrington',
     'CG Williams',
     'SD Hope',
     'Muhammad Musa',
     'JP Kotze',
     'BM Scholtz',
     'KS Leverock',
     'MS Dhoni',
     'AJ Staal',
     'S Snater',
     'SR Thompson',
     'Kuldeep Yadav',
     'CR Brathwaite',
     'JD Campbell',
     'MD Gunathilaka',
     'Hamza Tahir',
     'Usman Ghani',
     'PHKD Mendis',
     'RN ten Doeschate',
     'R Rampaul',
     'A Khan',
     'DAJ Bracewell',
     'CT Mutombodzi',
     'ZE Green',
     'Hasan Ali',
     'CJ Dala',
     'CR Ervine',
     'JT Smuts',
     'XM Marshall',
     "GH O'Brien",
     'PWH de Silva',
     'C Munro',
     'AR McBrine',
     'TG Southee',
     'Nurul Hasan',
     'GC Wilson',
     'Mujeeb Ur Rahman',
     'TS Mills',
     'BN Cooper',
     'Q de Kock',
     'Shafiul Islam',
     'N Pradeep',
     'D Pretorius',
     'EJG Morgan',
     'AT Carey',
     'JM Vince',
     'HC Overdijk',
     'Mohammad Shahzad',
     'CH Gayle',
     'T Banton',
     'RR Hendricks',
     'D Wiese',
     'D Ramdin',
     'CAK Rajitha',
     'SPD Smith',
     'DW Steyn',
     'DE Budge',
     'MS Wade',
     'YS Chahal',
     'Mohammad Hasnain',
     'R Ashwin',
     'Tamim Iqbal',
     'BR McDermott',
     'L Gregory',
     'Mohammad Mithun',
     'SO Hetmyer',
     'B Kumar',
     'JJ Tucker',
     'IS Sodhi',
     'UT Yadav',
     'Shafiqullah',
     'OGL Bascome',
     'DJ Bravo',
     'AK Markram',
     'Mohammad Naim',
     'Iftikhar Ahmed',
     'PADLR Sandakan',
     'IA Karim',
     'SO Ngoche',
     'CB Mpofu',
     'E Lewis',
     'KC Hodsoll',
     'C de Grandhomme',
     'DJM Short',
     'CK Tshuma',
     'DMW Rawlins',
     'Mustafizur Rahman',
     'Mohammad Nawaz (3)',
     'JA Richardson',
     'DC Stovell',
     'A Neill',
     'TC Bruce',
     'T Maruma',
     'Shoaib Malik',
     'CT Mumba',
     'BM Tickner',
     'JJ Smit',
     'TWM Latham',
     'A Nortje',
     'Najeeb Tarakai',
     'Khushdil Shah',
     'N Madziva',
     'BA King',
     'TL Seifert',
     'JN Frylinck',
     'AY Patel',
     'SS Iyer',
     'Imad Wasim',
     'RJ Trott',
     'OJ Hairs',
     'CA Young',
     'JDF Vandersay',
     'WT Mashinge',
     'AA Obanda',
     'M Simmons',
     'C Floyd',
     'F du Plessis',
     'SA Edwards',
     'Washington Sundar',
     'SW Billings',
     'Sikander Zulfiqar',
     'DJ Malan',
     'OF Smith',
     'TA Boult',
     'JR Hazlewood',
     'Hussain Talat',
     'Sharjeel Khan',
     'Afif Hossain',
     'BTJ Wheal',
     'HM Nicholls',
     'Fakhar Zaman',
     'GT Main',
     'H Klaasen',
     'AR Patel',
     'PBB Rajapaksa',
     'MJ Swepson',
     'W Madhevere',
     "KJ O'Brien",
     'Z Groenewald',
     'LH Ferguson',
     'S Kaul',
     'Shadab Khan',
     'DC Thomas',
     'Shakib Al Hasan',
     'MG Erasmus',
     'SC Kuggeleijn',
     'N Dickwella',
     'MJ Santner',
     'Sayed Shirzad',
     'RN Patel',
     'MA Wood',
     'KK Ahmed',
     'WIA Fernando',
     'Izatullah Dawlatzai',
     'KMA Paul',
     'A Zampa',
     'Mohammad Rizwan',
     'RA Jadeja',
     'PVD Chameera',
     'E Otieno',
     'Sohaib Maqsood',
     'B Fernando',
     'RG Sharma',
     'JW Dernbach',
     'AU Rashid',
     'Shapoor Zadran',
     'SS Cottrell',
     'AF Milne',
     'DA Miller',
     'Rahmanullah Gurbaz',
     'SL Malinga',
     'Mushfiqur Rahim',
     'Liton Das',
     'TP Visee',
     'RR Pant',
     'KS Williamson',
     'JDS Neesham',
     'SJ Myburgh',
     'N Davin',
     'AL Phehlukwayo',
     'JH Davey',
     'SE Rutherford',
     'BB Chari',
     'Asif Ali',
     'TS Chisoro',
     'W Barresi',
     'L Ngidi',
     'GSNFG Jayasuriya',
     'DC Delany',
     'CO Obuya',
     'K Rabada',
     'TE Kane',
     'A Dananjaya',
     'JC Archer',
     'BOP Fernando',
     'FJ Klaassen',
     'AK Perera',
     'AD Mathews',
     'K Pierre',
     'P Kerai',
     'PR Brown',
     'LA Dawson',
     'KW Richardson',
     'TK Musakanda',
     'Karim Janat',
     'JJ Roy',
     'RE van der Merwe',
     'A Ndlovu',
     'Haris Rauf',
     'K Birkenstock',
     'CB Sole',
     'KOK Williams',
     'JM Bairstow',
     'AJ Finch',
     'E Ochieng',
     'Umar Akmal',
     'Saqib Zulfiqar',
     'N Pooran',
     'T Lungameni',
     'MA Leask',
     'KJ Coetzer',
     'MW Parkinson',
     'MO Jones',
     'A Balbirnie',
     'Mohammad Nabi',
     'NA Saini',
     'Sharafuddin Ashraf',
     'HD Rutherford',
     'PRP Boissevain',
     'CJ Chibhabha',
     'GJ Maxwell',
     'Mohammed Shami',
     'CJ Jordan',
     'TM Head',
     'MRJ Watt',
     'LM Jongwe',
     'RP Burl',
     'RW Chakabva',
     'O Bascome',
     'PSP Handscomb',
     'Wahab Riaz',
     'C Viljoen',
     'Shaheen Shah Afridi',
     'FA Allen',
     'Mohammad Saifuddin',
     'SN Thakur',
     'BKG Mendis',
     'AR Gandhi',
     'KL Rahul',
     'R Powell',
     'AC Agar',
     'PM Seelaar',
     'MD Shanaka',
     'PA van Meekeren',
     'DM de Silva',
     'KM Jarvis',
     'DJ Mitchell',
     'MC Henriques',
     'SC Williams',
     'SW Poynter',
     'CBRLS Kumara',
     'TK Curran',
     'OC McCoy',
     'Mahmudullah',
     'TD Astle',
     'GH Dockrell',
     'DT Tiripano',
     'H Masakadza',
     'L Louwrens',
     'SJ Baard',
     'JP Behrendorff',
     'Mahedi Hasan',
     'Qais Ahmad',
     'OO Bascome',
     'R Ngarava',
     'MK Pandey',
     'R Shepherd',
     'CR Woakes',
     'RD Chahar',
     'DM Gondaria',
     'GJ Delany',
     'M Bhanuka',
     'BE Hendricks',
     'Ahsan Ali',
     'RAJ Smith',
     'Fazal Niazai',
     'WP Masakadza',
     'BRM Taylor',
     'S Mahmood',
     'Fareed Ahmad',
     'Taijul Islam',
     'HT Tector',
     'CD Wallace',
     'DA Warner',
     'Babar Azam',
     'T van der Gugten',
     'MJ Guptill',
     'Rashid Khan',
     'SF Mire',
     'GD Phillips',
     'MR Adair',
     'LMP Simmons',
     'LN Oluoch',
     'Mohammed Siraj',
     'TS Braat',
     'NN Odhiambo',
     'S Samarawickrama',
     'MR Marsh',
     'B Stanlake',
     'Vikramjit Singh',
     'Sikandar Raza',
     'HN Ya France',
     'DM Bravo',
     'S Smith',
     'BFW de Leede',
     'TS Fray',
     'JC Buttler',
     'MA Starc',
     'Mohammad Amir',
     'SM Curran',
     'MDKJ Perera',
     'DL Brangman',
     'Sabbir Rahman',
     'Dawlat Zadran',
     'PR Stirling',
     'MH Cross',
     'J Theron',
     'B Shikongo',
     'O Thomas',
     'JN Malan',
     'AD Russell',
     'SC Getkate',
     'Mohammad Irfan',
     'Ahmed Shehzad',
     'AC Douglas',
     'SHA Rance',
     'L Sipamla',
     'HH Pandya',
     'KH Pandya',
     'JE Pitcher',
     'MM Ali')
    player = st.selectbox("Player", players_list)
    show_performance = st.button("Show")
    
    if show_performance:
        st.write("""#### Overall performance""")
        overall_performance = pd.DataFrame({
        'Player': [player],
        'Innings Batted': [players_innings_batted[player]],
        'Batting Avg.': [batting_avg[player]],
        'Century Innings': [century_innings[player]],
        'fifty Innings': [fifty_innings[player]],
        'Zeros Innings': [zeros_innings[player]],
        'Highest score': [highest_score[player]],
        'Batting SR': [strike_rate_bat[player]],
        'Innings Bowled': [players_innings_bowled[player]],
        'Total Overs Bowled': [no_inn_bowled[player]],
        'Bowling Avg.': [bowling_avg[player]],
        'Four-Five Wickets': [FF[player]],
        'Bowling SR': [strike_rate_bowl[player]],
        'Bat Consistency': [consistency[player][0]],
        'Bowl Consistency': [consistency[player][1]]
        })
        st.write(overall_performance)
        

        plot_col_1, plot_col_2 = st.columns([3,3])
        
        
        #batting radar graph
        categories = ['Innings Batted', 'Batting Avg.', 'Batting SR', 'Bat Consistency']
        categories = [*categories, categories[0]]

        player_1 = [players_innings_batted[player], batting_avg[player],  strike_rate_bat[player], consistency[player][0]]
        player_1 = [*player_1, player_1[0]]
       
        fig = go.Figure(
            data=[
                go.Scatterpolar(r=player_1, theta=categories, fill = 'toself', name=player),
            ],
            layout=go.Layout(
                title=go.layout.Title(text='Batting Stats'),
                polar={'radialaxis': {'visible': True}},
                showlegend=True
            )
        )

        plot_col_1.plotly_chart(fig)

        #bowling radar graph
        categories = ['Innings Bowled', 'Bowing Avg.', 'Bowling SR', 'Bowl Consistency']
        categories = [*categories, categories[0]]

        player_1 = [players_innings_bowled[player], bowling_avg[player], strike_rate_bowl[player], consistency[player][1]]
        player_1 = [*player_1, player_1[0]]
       
        fig = go.Figure(
            data=[
                go.Scatterpolar(r=player_1, theta=categories, fill = 'toself', name=player),
            ],
            layout=go.Layout(
                title=go.layout.Title(text='Bowling Stats'),
                polar={'radialaxis': {'visible': True}},
                showlegend=True
            )
        )

        plot_col_2.plotly_chart(fig)


        player_data = extract_oppo(against_oppo_df, player)
        st.write("""#### Performance Against Teams""")
        ag_op_performance = pd.DataFrame({
        'Team': [i[1] for i in player_data],
        'Innings Played': [i[2] for i in player_data],
        'Batting Avg.': [i[3] for i in player_data],
        'Bowling Avg.': [i[4] for i in player_data],
        'Centuries': [i[5] for i in player_data],
        'fifties': [i[6] for i in player_data],
        'zeros': [i[7] for i in player_data],
        'Highest score': [i[8] for i in player_data],
        'Batting SR': [i[9] for i in player_data],
        'Bowling SR': [i[10] for i in player_data],
        'Four-Five Wickets': [i[11] for i in player_data],
        })
        st.write(ag_op_performance)

        # visualize = st.selectbox()
        st.write("""### Averages """)
        col1,col2 = st.columns([3,3])
        data = ag_op_performance.groupby(['Team'])['Batting Avg.'].mean().sort_values(ascending=True)
        col1.bar_chart(data)
        
        data = ag_op_performance.groupby(['Team'])['Bowling Avg.'].mean().sort_values(ascending=True)
        col2.bar_chart(data)
        

        st.write("""### Strike Rates """)
        col3,col4 = st.columns([3,3])
        data = ag_op_performance.groupby(['Team'])['Batting SR'].mean().sort_values(ascending=True)
        col3.bar_chart(data)
        
        data = ag_op_performance.groupby(['Team'])['Bowling SR'].mean().sort_values(ascending=True)
        col4.bar_chart(data)


        

        