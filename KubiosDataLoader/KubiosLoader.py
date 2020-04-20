import pandas as pd


class KubiosDataLoading:
    """"Creating a dictionary with data frame of the elements from kubios data
    :parameter kubios data = .txt file from kubios system
    :return dictionary with data frames of kubios different parts of calculations , for example time varying results"""
    def __init__(self, kubios_data):
        self.data = kubios_data
        self.whole_data = pd.DataFrame()
        self.dict_sections = {}

    def openfile(self):
        """" Read in the kubios text file as a pandas data frame to be able to use it for splitting the elements"""
        with open(self.data, "r") as f:
            data_lines = f.readlines()
        whole_data = pd.DataFrame([string.split(",") for string in data_lines])
        title = ["kubios data input"]
        end = ["end of document"]
        whole_data = pd.concat([pd.DataFrame(title), whole_data], ignore_index=True)
        whole_data = whole_data.append(end, ignore_index=True)
        self.whole_data = whole_data.replace('\n', '', regex=True)

    def splitting(self):
        """"Splitting the whole data set in different sections for analysis and create dict with all values"""
        def creating_section(data, start, end):
            """ Function to get index value for begin and end of split to be able to divide data set in
            different sections"""
            row_begin = data.loc[data[0] == start].index.tolist()
            row_ends = data.loc[data[0] == end].index.tolist()
            section_data = data.iloc[row_begin[0]:row_ends[0]]
            return section_data
        sections = {
            "general_information": ["kubios data input", "Parameters"],
            "parameters_and_options": ["Parameters", "RR Interval Samples Selected for Analysis"],
            "sample_selection": ['RR Interval Samples Selected for Analysis', "RESULTS FOR A SINGLE SAMPLE"],
            "results_single_sample": ["RESULTS FOR A SINGLE SAMPLE", "TIME-VARYING RESULTS          "],
            "time_varying_results": ["TIME-VARYING RESULTS          ", "RR INTERVAL DATA and SPECTRUM ESTIMATES"],
            "rr_interval_and_spectrum": ["RR INTERVAL DATA and SPECTRUM ESTIMATES", "end of document"]
        }
        dict_sections = {}
        for section, split_point in sections.items():
            """" loop to establish dict with all data frames for the kubios data of the sections that are 
            defined in the sections """
            section_data_loop = creating_section(self.whole_data, split_point[0], split_point[1])
            section_data_loop.is_copy = None
            section_data_loop.replace([""], [None], inplace=True)
            pd.DataFrame.dropna(section_data_loop, axis=1, how="all", inplace=True)
            section_data_loop.replace([None], [""], inplace=True)
            dict_sections["{}".format(section)] = section_data_loop
        self.dict_sections = dict_sections

    def optimizing_sections(self, zones_drop=True):
        """" Optimizing sections to be used for machine learning algorithm , now only the time series section is
        prepared for machine learning
        if zones_drop is false the zones section of the time series is saved """
        time_varying_results = self.dict_sections["time_varying_results"]
        time_varying_results = time_varying_results.drop(0, 1).drop(time_varying_results.head(3).index)
        time_varying_results.iloc[0] = time_varying_results.iloc[0] + time_varying_results.iloc[1].str.strip()
        time_varying_results.drop(time_varying_results.index[1], inplace=True)
        if zones_drop:
            time_varying_results = time_varying_results.drop(time_varying_results.tail(18).index).drop([40], axis=1)
        time_varying_results.columns = time_varying_results.iloc[0].str.strip()
        time_varying_results = time_varying_results.drop(time_varying_results.index[0]).astype(str)\
            .apply(lambda x: x.str.strip())
        time_varying_results["datetime"] = pd.to_datetime(time_varying_results["Time(hh:mm:ss)"], format="%H:%M:%S")\
            .dt.time
        time_varying_results = time_varying_results.set_index("datetime").drop(["Time(hh:mm:ss)"], axis=1)\
            .astype(float)
        self.dict_sections["time_varying_results"] = time_varying_results

    def kubios_data_extraction(self, zones_drop=True):
        """"total function to conduct kubios data extraction"""
        self.openfile()
        self.splitting()
        self.optimizing_sections(zones_drop)
        return self.dict_sections
