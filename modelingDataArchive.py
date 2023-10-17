import pandas as pd
import sys
import os
import numpy as np
import itertools
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
from scipy.optimize import curve_fit
from datetime import date, timedelta, time, datetime
from sklearn.linear_model import LinearRegression
from dataArchive import DataArchive
from datetime import date, timedelta, time, datetime

class Model():
    """
    A class that models something
    ...
    
    Attributes
    ----------
    None--receives from command line/init file
        
    Methods
    -------
    
    """
    
    def __init__ (self):
        """
        Class constructor
        
        Args:
            
        """
        data = self._get_data_archive()
        self._prep_data(data)
        
    
    def _get_data_archive(self):
        tel = #Tel number
        dataArch = DataArchive(tel)
        daynum = #number of days of data
        channel_1 = #channel name
        channel_2 = #second channel name 
        *whatever data the channel provides* = dataArch.getData(channel_1, *timeperiod*, nrSecs=*number of seconds*)
        name, xp, yp = dataArch.getData(channel_2, (datetime.now() - timedelta(days = daynum)), nrSecs=*number of seconds*)
        data = np.array(xp,yp) #for example
        '''
        Clean Data Here
        '''
        return data
           
    
    def _get_time (self, day_length = 112):
        self.times = []
        self.times = np.arange(0,24,(24/day_length))
    
    def resample_intervals(self, data, bin_size_secs=600):
        """
        Resamples the data into bins of bin_size_secs.
        Returns new list.
        """

        rows = []
        t0 = data[0][0]
        tref = t0
        cnt = 0
        sum0 = 0
        secs = 0
        for row in range(len(data[0])):
            ts, data = data[0][row],data[1][row]
            dt = ts - t0
            if dt >= bin_size_secs:
                secs = t0 + bin_size_secs // 2
                hour = (secs - tref) / 3600
                new_row = datetime.utcfromtimestamp(secs).strftime('%Y-%m-%d %H:%M:%S'), hour, sum0 / cnt
                rows.append(new_row)
                sum0 = data
                cnt = 1
                t0 = ts
            else:
                cnt += 1
                sum0 += data
        if cnt > 1:
            secs = t0 + bin_size_secs // 2
            hour = (secs - tref) / 3600
            rows.append((datetime.utcfromtimestamp(secs).strftime('%Y-%m-%d %H:%M:%S'), hour, sum0 / cnt))
        return rows

            
    def _prep_data (self, data):
        '''
        Prep the data and set self.data to the data
        '''
        self.data = data
    
    
    
    def predict (self):
        """
        Function to create the model based on ingested data and parameters

        Args:
            none

        Returns:
            arr: array of predictions
        """
        
        return predictions
        
                  
        
    def _daterange(self, start_date, end_date):
        """
        creates a range of dates to be iterated over
        """
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)
        
    def plot (self, filename = "WritePredictionHere.html"):
        """
        Plots the model predictions
        Args:
            none--specified in the command line
            
        Returns:
            none
        """
        df1 = pd.DataFrame()
        df2 = pd.DataFrame() #create dataframes with the prediction data and any actual data you have to be plotted
        fig1 = px.scatter(df1, x = x1, y = y1, color_discrete_sequence = ['#63C3E1'], symbol_sequence = ['circle-open'], trendline = "lowess", trendline_options = dict(frac = (0.05))) #examples of trendline, symbol, etc
        fig2 = px.scatter(df2,x = x2, y = y2, color_discrete_sequence= ['#D09184'], symbol_sequence = ['triangle-up-open'])
        fig = go.Figure(data = fig2.data + fig1.data) #combine figures in plotly
        fig.update_layout(
            showlegend = True,
            width = (700 + (100 * plots)),
            height = 500,
            title="Outside Temperature Prediction",
            xaxis_title="Date",
            yaxis_title="Temperature",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#4a148c"
                )
            )
        pio.write_html(fig, file=filename, auto_open=False, full_html=False, include_plotlyjs=True)
        fig.show()

if __name__ == "__main__":
    '''
    Receive input from the command line when you run the file
    '''
    import argparse
    def parseArguments(in_args):
        description = "File that models something"
        usage = "\n{} [-a Arg1] [-b Arg1] [-c Arg1]\n".format(in_args[0])
        epilog = "file located at: \"WritePredictionHere.html\""

        parser = argparse.ArgumentParser(description=description, usage=usage, epilog=epilog)
        parser.add_argument("-a", "--Arg1", dest="variable_name", help="description of variable", type=datatype, default=defaultvalue)
        parser.add_argument("-b", "--Arg2", dest="variable_name2", help="description of variable", type=datatype, default=defaultvalue)
        parser.add_argument("-c", "--Arg3", dest="variable_name3", help="description of variable", type=float, default=18.5)
        
        args = None
        try:
            args = parser.parse_args(in_args[1:])
        except Exception as e:
            print(e)
            parser.print_help()
            sys.exit(0)
        return args
    args = parseArguments(sys.argv)
    model = Model(param1 = args.variable_name, param2 = args.variable_name2, param3 = args.variable_name3)
    model.plot()