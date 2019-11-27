import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.core.display import HTML,display,Javascript,Markdown,Latex
#%matplotlib inline

df = pd.read_csv("train.csv")

def general_stats (df):
    '''This function take a dataframe and will display and plot several statistics about the dataframe.'''
    j=1
    L=[]
    display(Markdown('<div class="alert alert-info"><center><h3>General Informations about the dataframe</h3></center> </div>'))
    shape = df.shape
    print("There are",shape[1],"different columns and",shape[0],"lines")
    print("\n")
    for i in df.columns:
        String = '<center><h7> Column number '+ str(j) + ' : <b>'+ str(i) +'</b></h7></center>'
        display(Markdown('<div class="alert alert-info">' + String + '</div>'))

        j+=1
        if df[i].dtype == 'int64' or df[i].dtype == 'float64': # Numerical columns
            stats = df[i].describe()
            

            print('Numerical columns')
            print("\n")
            print('general statistics:')
            display_stats(df,i)            
            
            print("\n")
            n_unique = df[i].nunique()
            if n_unique <= 5:
                donut_plot(df,i)

            elif stats['std']<100:
                plot_hist(df,i,25)

            else:
                print("Is it an ID? An index ?")
                print("Here are the first values:")
                mini_df = serie_to_df(df[i].head(5),i)
                pandas_df_to_markdown_table(mini_df)
                
            L.append(i)
            
            
        else :  # Non numerical columns                     
            if len(df[i].unique()) <= 50:
                values = df[i].value_counts()
                print('Non numerical column')
                print("\n") 
                print('value counts:')
                pandas_df_to_markdown_table(serie_to_df(values,'values'))
                print("\n") 
                donut_plot(df,i)
            else :
                print('This column presents a big amount of different non numerical values, is it an id ? A name ?')
                print('here is a sample:')
                print("\n")
                mini_df = serie_to_df(df[i].head(10),i)
                pandas_df_to_markdown_table(mini_df)
        
        nan_count = df[i].isna().sum()  
        if nan_count!=0:
            print("\n")
            String='<center><h7>Be aware that there are ' + str(nan_count) + ' nan in this column<h7><center>'
            display(Markdown('<div class="alert alert-danger">' + String + '</div>'))
        print("\n")

    String='<center><h7> About the numerical values, here is the correlation table <h7><center>'
    display(Markdown('<div class="alert alert-info">' + String + '</div>'))
    plt.matshow(df[L].corr())
    plt.xticks(range(len(L)), L)
    plt.yticks(range(len(L)), L)
    plt.colorbar()
    plt.show()

        
#general_stats(df)       

def donut_plot(df,i):
    
    legend = []
    data=[]

    for l,x in enumerate(df[i].value_counts()):
        legend.append(str(i) + ' = ' + str(df[i][l]))
        data.append(x)
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-90)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for m, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(legend[m], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)

    ax.set_title("Donut plot "+str(i))

    plt.show()  

def pandas_df_to_markdown_table(df):
    from IPython.display import Markdown, display
    fmt = ['---' for i in range(len(df.columns))]
    df_fmt = pd.DataFrame([fmt], columns=df.columns)
    df_formatted = pd.concat([df_fmt, df])
    display(Markdown(df_formatted.to_csv(sep="|", index=False)))

def serie_to_df(ser,i):
    
    df2 = pd.DataFrame({
        "index":ser.index,
        str(i): ser.values
    })
    return df2

def plot_hist(df,column,bins):
    from matplotlib.ticker import StrMethodFormatter

    ax = df.hist(column=column, bins=bins,  figsize=(6,4), color='#86bf91', zorder=2, rwidth=0.9)

    ax = ax[0]
    for x in ax:

        # Despine
        x.spines['right'].set_visible(False)
        x.spines['top'].set_visible(False)
        x.spines['left'].set_visible(False)

        # Switch off ticks
        x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

        # Draw horizontal axis lines
        vals = x.get_yticks()
        for tick in vals:
            x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

        # Remove title
        x.set_title("")

        # Set x-axis label
        x.set_xlabel("value of column "+str(column), labelpad=20, weight='bold', size=12)

        # Set y-axis label
        x.set_ylabel("frequence", labelpad=20, weight='bold', size=12)

        # Format y-axis label
        x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))
    plt.show()

def display_stats(df,column):
    desc = df[column].describe()
    df2 = pd.DataFrame({
            "index":desc.index,
            str(column): desc.values
        }).set_index("index")
    pandas_df_to_markdown_table(df2.round(1).T)