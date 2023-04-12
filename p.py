import streamlit as st

# Set page title
st.set_page_config(layout='wide',page_title='Aman Sharma - Business Analyst')

tab1, tab2, tab3 = st.tabs(["Home","About me", "Projects"])

#Home
with tab1:

    title_spc, title, pp,ppspc = st.columns((.75,2,2,.25))
    with title:
        st.title("")
        st.title("")
        st.subheader("Hi! I am")
        st.title(":blue[Aman] Kumar Sharma")
        st.markdown("Hi, My name is Aman, I am a full time Business Analyst with over 1.5 years of expereince. Juggling around the data problems and crunching out numbers is what I do best. Weather it is a web app, superwised machine learning, exploratory data analysis or beautiful dashboards, my portfolio consists all. Do have a look around !!")
        link,git, resume1,logospc = st.columns((.2,.2,.8,.8))
        with link:
            st.markdown('[![LinkedIn](https://img.icons8.com/color/48/000000/linkedin-circled--v1.png)](https://www.linkedin.com/in/amankrsharma23/)')
        with git:
            st.markdown('[![GitHub](https://img.icons8.com/material-rounded/48/000000/github.png)](https://github.com/amanksharma23)')
        resume,resspc,resspc = st.columns((.4,.8,.8))
        
        with open("Aman sharma.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        
        
        with resume:
            st.text("")
            st.download_button(
                label="Resume",
                data=PDFbyte,
                file_name= "Aman sharma.pdf",
                mime='pdf',
            )
        
        st.markdown("______________________________________________________________________________________")

    with pp:
        st.image('Propic1680178080640-01.jpeg')

    st.markdown("<h1 style='text-align: center; color: #3396ff;'>Portfolio</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: black; font-size: 28px'>My projects</h1>", unsafe_allow_html=True)
    st.markdown("_________________________________________________")
    
    edaapp ,credit, dashboard = st.columns((1,1,1))
    
    with edaapp:
        hyperlink_url = 'https://amanksharma23-data-app-eda-nb98qh.streamlit.app/'
        st.image("Screenshot (8).png")
        st.markdown(f'<a href="{hyperlink_url}"><h1 style="text-align: center; color: black; font-size: 28px">Exploratory data analysis app</h1></a>', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #31333F; font-size: 16px'>An app that enables you to do the exploratory data analysis within few minutes.</h2>", unsafe_allow_html=True)
    
    with credit:
        hyperlink_url2 = 'https://colab.research.google.com/drive/1jIo3tkHQ0W9GvoaOZ3tBZHOXU634WxF3#scrollTo=e24bXv2CosnV'
        st.image("2903788.jpg")
        st.markdown(f'<a href="{hyperlink_url2}"><h1 style="text-align: center; color: black; font-size: 28px">Credit card default prediction</h1>', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #31333F; font-size: 16px'>Created a model for prediction of default customers using Machine learning in Python.</h2>", unsafe_allow_html=True)
    
    with dashboard:
        hyperlink_url3 = 'https://1drv.ms/p/s!AsL2nk73rYBIgj19fP0918tiGtdS?e=VIojBo'
        st.image("Screenshot_20221216_082322.png")
        st.markdown(f'<a href="{hyperlink_url3}"><h1 style="text-align: center; color: black; font-size: 28px">Power Bi and Looker Studio Dashboards</h1>', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #31333F; font-size: 16px'>A quick glance at my dashboards that presents useful insights.</h2>", unsafe_allow_html=True)

#Projects
with tab3:
    
    st.title(":blue[Pro]jects")
    edaapp1,edadesspc, edasum = st.columns((2,.20,2.60))
    credsum, creddesspc,credit1= st.columns((2.60,.20,2))
    dashboard1,dashdesspc,dashsumn = st.columns((2,.20,2.60))
    rosssum,rossspc,ross1 = st.columns((2.60,.20,2))
    hotel1,hotelspc,hotelsum = st.columns((2,.20,2.60))

    with edaapp1:
        hyperlink_url = 'https://amanksharma23-data-app-eda-nb98qh.streamlit.app/'
        st.image("Screenshot (8).png")
        st.markdown(f'<a href="{hyperlink_url}"><h1 style="text-align: center; color: black; font-size: 28px">Exploratory data analysis app</h1></a>', unsafe_allow_html=True)
        st.markdown("__________________________________")   
    with edasum:  
        st.subheader("An app that enables you to do the exploratory data analysis within few minutes.")  
        st.markdown("At a glance what this web app does :")
        st.markdown("1. It Identifies the data types int, float, str and datetime.")
        st.markdown("2. Then categorize the whole dataset into dimensions (categorical), dates and metrics (numerical).")
        st.markdown("3. Extract month num and year from dates for the user to observe trends dynamically.")
        st.markdown("4. Then it moves further to help user understand the data better by applying Principal component analysis (PCA).")
        st.markdown("5. So in a nutshell you will be able to figure out where to look in a data set through PCA.")

    with credit1:
        hyperlink_url2 = 'https://colab.research.google.com/drive/1jIo3tkHQ0W9GvoaOZ3tBZHOXU634WxF3#scrollTo=e24bXv2CosnV'
        st.image("2903788.jpg")
        st.markdown(f'<a href="{hyperlink_url2}"><h1 style="text-align: center; color: black; font-size: 28px">Credit card default prediction</h1>', unsafe_allow_html=True)
        st.markdown("______________________________________________")
    with credsum:
        st.subheader("Created a model for prediction of default customers using Machine learning in Python.")
        st.markdown("1. Here I have used logistic regression and Decision tree method for the prediction.")
        st.markdown("2. Used one hot encoding to engineer the model for accuracy.")
        st.markdown("3. And finally compared the model accurcay.")
        st.markdown("4. My next step for this project will be to deploy the model on cloud.")

    with dashboard1:
        hyperlink_url3 = 'https://1drv.ms/p/s!AsL2nk73rYBIgj19fP0918tiGtdS?e=VIojBo'
        st.image("Screenshot_20221216_082322.png")
        st.markdown(f'<a href="{hyperlink_url3}"><h1 style="text-align: center; color: black; font-size: 28px">Power Bi and Looker Studio Dashboards</h1>', unsafe_allow_html=True)
        st.markdown("_________________________________________")     
    with dashsumn:
        st.subheader("A quick glance at my dashboards that presents useful insights.")
        st.markdown("1. Used PowerBi and excel data source to create the dashboard.")
        st.markdown("2. Converted the financial model to structured data in order to analyse.")
        st.markdown("3. Analysed the revenue, fixed cost, variable cost of a real estate company.")

    with ross1:
        hyperlink_url3 = 'https://colab.research.google.com/drive/12R24UfAGKGTv89eFBJhzhgaMryv5-FZU'
        st.image("rossman.png")
        st.markdown(f'<a href="{hyperlink_url3}"><h1 style="text-align: center; color: black; font-size: 28px">Rossmann Sales Prediction</h1>', unsafe_allow_html=True)
        st.markdown("_________________________________________")
        
    with rosssum:
        st.subheader("A project on Supervised Machine Learning- Regression.")
        st.markdown("1. With the help of Facebook prophet algorithm that follows the additive regression method to predict the dependent variable taking into consideration the change in independent variable.")
        st.markdown("2. Detected anomalies and handeled null values.")
        st.markdown("3. Predicted the sales of the store taking consideration into the holidays.")

    with hotel1:
        hyperlink_url3 = 'https://colab.research.google.com/drive/1LEO4t5ewIxe61t6sEZRi6MPaaNv5qgQ_'
        st.image("hotel.png")
        st.markdown(f'<a href="{hyperlink_url3}"><h1 style="text-align: center; color: black; font-size: 28px">Hotel Booking Data Analysis</h1>', unsafe_allow_html=True)
        st.markdown("_________________________________________")
        
    with hotelsum:
        st.subheader("This project focuses on Exploratory data analysis of a hotel booking data set.")
        st.markdown("1. Using matplotlib and seaborn plotted graphs that presents useful insights for each hotel.")
        st.markdown("2. Handeled null values and replaced it with the respective averages to get the unbiased insights.")

#Sum
with tab2:

    spcer,sumtit,logo2,spc47,spc38 =st.columns((1.75,1,.3,1,1))
    with sumtit:
        st.title("Carrer :blue[Path]")
    with logo2:
        st.markdown("")
        st.image("racing (1).png")


    lpspc,lpcont,grapht,lpspc2 = st.columns((.75,2,.5,1))
    with grapht:
        st.title("")
        st.title("")
        st.image("number-3.png")
    with lpcont:
        with st.container():
            # Set the background color and font color
            st.markdown("""
                <style>
                .box {
                    background-color: #BED8F7;
                    color: black;
                    padding: 10px;
                    border-radius: 5px;
                    box-shadow: 2px 2px 5px grey;
                }
                </style>
                """, unsafe_allow_html=True)
            # Add text to the container
        st.markdown('<div class="box"><b></p>July 2023</b></p>'
                    '<b><p>And now I am currently working as a business analyst at Legistify.</b></p>'
                    '<ul>'
                    '<li>Analyzing the SAAS based products of the company (Product Usage Analytics).</li>'
                    '<li>Developing dashboards for the stakeholders in accordance with their needs.</li>'
                    '<li>Further maintaining the dashboards and drawing useful insights to further take data driven decisions.</li>'
                    '</ul></div>', unsafe_allow_html=True) 
    lpspc2,grapht2,lpcont2,lpspc3 = st.columns((1,.5,2,1))
    with grapht2:
        st.title("")
        st.image("number-2.png")
    with lpcont2:
        with st.container():
            # Set the background color and font color
            st.markdown("""
                <style>
                .box {
                    background-color: #BED8F7;
                    color: black;
                    padding: 10px;
                    border-radius: 5px;
                    box-shadow: 2px 2px 5px grey;
                }
                </style>
                """, unsafe_allow_html=True)
            # Add text to the container
        st.markdown('<div class="box"><p><b>June 2022 </b></p>'
                    '<ul>'
                    '<p>Completed my graduation along with that created some projects in python, PowerBi and Excel.</p>'
                    '<ul>'
                    '<p>That further got me my first job as a Business Analyst</p>'
                    '</ul></div>', unsafe_allow_html=True) 
    lpspc3,lpcont3,grapht3,lpspc3 = st.columns((.75,2,.5,1))
    with grapht3:
        st.title("")
        st.title("  ")
        st.image("number-one.png")
    with lpcont3:
        with st.container():
            # Set the background color and font color
            st.markdown("""
                <style>
                .box {
                    background-color: #BED8F7;
                    color: black;
                    padding: 10px;
                    border-radius: 5px;
                    box-shadow: 2px 2px 5px grey;
                }
                </style>
                """, unsafe_allow_html=True)
            # Add text to the container
        st.markdown('<div class="box"><p><b>April 2021 - May 2022 </b></p>'
                    '<ul>'
                    '<p><b>While studying finance in my graduation and pursuing some courses through youtube about Python, Excel and PowerBI.</b></p>'
                    '<ul>'
                    '<p>I interned at Lavero Infrastructures, Brainquest Consulting and Natureship Foods as an Analyst</p>'
                    '<ul>'
                    '<li>Where I learned the most about what I am doing now.</li></ul></div>', unsafe_allow_html=True)


    
    
    st.markdown("<h1 style='text-align: center; color: #3396ff;'>My skills</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #4C4E54;font-size: 14px'>Here are my skills with the level as stars are provided, 5 star being the highest.</h1>", unsafe_allow_html=True)
    skillspc, python, sql, microsoft_excel, powerbi,Looker, skillsspc2 = st.columns((0.65,0.9,0.9,0.9,0.9,0.9,0.25))
    spc45,tableau,ml,prdana,desst,etl,spc46 = st.columns((0.65,0.9,0.9,0.9,0.9,0.9,0.25))

    with python:
        st.markdown("")
        python.markdown("Python")
        st.markdown(":star::star::star::star:")

    with sql:
        st.markdown("")
        sql.markdown("SQL")
        st.markdown(":star::star::star:")
    with microsoft_excel:
        st.markdown("")
        microsoft_excel.markdown("Microsoft Excel")
        st.markdown(":star::star::star::star::star:")

    with powerbi:
        st.markdown("")
        powerbi.markdown("PowerBi")
        st.markdown(":star::star::star::star:")

    with Looker:
        st.markdown("")
        st.markdown("Looker Studio")
        st.markdown(":star::star::star::star:")

    with tableau:
        st.markdown("")
        st.markdown("Tableau")
        st.markdown(":star::star::star:")

    with ml:
        st.markdown("")
        st.markdown("Machine Learning")
        st.markdown(":star::star:")

    with prdana:
        st.markdown("")
        st.markdown("Predictive Analysis")
        st.markdown(":star::star::star::star:")

    with desst:
        st.markdown("")
        st.markdown("Descriptive Statistics")
        st.markdown(":star::star::star::star:")

    with etl:
        st.markdown("")
        st.markdown("Export Transform Load")
        st.markdown(":star::star::star::star:")