
import numpy as np
import pandas as pd


def bin_departure_delays(delay_min):
    if delay_min <= 15:
        return "no_delay"
    elif (delay_min > 15) & (delay_min <= 30):
        return "small_delay"
    elif (delay_min > 30) & (delay_min <= 60):
        return "medium_delay"        
    elif (delay_min > 60) & (delay_min <= 120):
        return "big_delay"        
    elif (delay_min > 120):
        return "compensated_delay"        
    else:
        return "missing_delay"


def delays_requiring_compensation(arrival_delay, departure_delay):
    """Fcn to return if arrival and/or departure delay resulted in passenger
       compensation.
       
       Arguments:
           - arrival_delay:   delay in minutes
           - departure_delay: delay in minutes
       
       Returns:
           - number of delays (arrival and or departure) that were delayed
             so long that passenger got compensated
    """
    count = 0
    if (arrival_delay/60.0 >= 3) | (departure_delay/60.0 >= 2):
        # If arrival delay is 3+ hours, or if departure delay is 2+ hours:
        count += 1
    return count


get_ipython().run_cell_magic('time', '', "df['compensated_delays'] = df[['ArrDelay', 'DepDelay']].apply(\n    lambda row: delays_requiring_compensation(row[0], row[1]),\n    axis=1)")
def delays_requiring_compensation_vec(arrival_delay, departure_delay):
    """Fcn to return if arrival and/or departure delay resulted in passenger
       compensation.
       
       Arguments:
           - arrival_delay:   delay in minutes
           - departure_delay: delay in minutes
       
       Returns:
           - number of delays (arrival and or departure) that were delayed
             so long that passenger got compensated
    """
    count_arrival_delays = arrival_delay >= (3 * 60.0)
    count_depaprture_delays = departure_delay >= (2 * 60.0)
    # Leveraging Boolean logic:
    compensated_delays = count_arrival_delays | count_depaprture_delays
    return compensated_delays


get_ipython().run_cell_magic('time', '', "df['compensated_delays_vec'] = delays_requiring_compensation_vec(df['ArrDelay'], df['DepDelay'])")
file_name = "https://s3.amazonaws.com/h2o-airlines-unpacked/year2012.csv"
# file_name = "../Class3/2012.csv"
df = pd.read_csv(filepath_or_buffer=file_name,
                 encoding='latin-1',
                 nrows=100)
# Replace times of cancelled flights with value 9999:
df['DepDelay'] = df['DepDelay'].fillna(9999)
df['ArrDelay'] = df['ArrDelay'].fillna(9999)


get_ipython().run_cell_magic('time', '', "df['compensated_delays_vec_np'] = delays_requiring_compensation_vec(df['ArrDelay'].values, df['DepDelay'].values)")


