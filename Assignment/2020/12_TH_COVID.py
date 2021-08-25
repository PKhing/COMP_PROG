# Prog-12: COVID-19: The Latest Wave
# 6?3?????21 Name ?
import numpy as np
def read_data(filename):
    d = np.loadtxt(filename, delimiter=",", encoding='utf-8', dtype=str)
    new_cases = np.array(d[1:,1:], dtype=int)
    norm = new_cases / np.max(new_cases, axis=1).reshape((new_cases.shape[0],1))
    return {'new_cases': new_cases,
    'norm_data': norm,
    'province_names': d[1:,0],
    'dates': d[0,1:]}
def max_new_cases_date(data):
    sum_case = data['new_cases'].sum(axis = 0)
    max_val = sum_case.max()
    max_date = data['dates'][sum_case == max_val]
    return (max_date[0],max_val)
def max_new_cases_province(data, beg_date, end_date):
    st = np.where(data['dates']==beg_date)[0][0]
    ed = np.where(data['dates']==end_date)[0][0]
    sum_case = data['new_cases'][:,st:ed+1].sum(axis = 1)
    max_val = sum_case.max()
    max_province = data['province_names'][sum_case==max_val]
    return (max_province[0],max_val)
def max_new_cases_province_by_dates(data):
    result = data['dates']
    max_new_case = data['new_cases'].max(axis = 0)
    province_list = np.where(data['new_cases'].T == np.array([max_new_case]).T)
    province_list = data['province_names'][province_list[1]]
    result= np.append(result,province_list)
    result = np.append(result,max_new_case)
    result.resize(3,len(data['dates']))
    return result.T
def most_similar(data, province):
    province_index = np.where(data['province_names']==province)
    province_norm_data = data['norm_data'][province_index]
    norm_data = np.delete(data['norm_data'],province_index,axis = 0)
    norm_data = (norm_data - province_norm_data)**2
    diff = np.sum(norm_data,axis = 1)
    min_province = np.delete(data['province_names'],province_index)[diff == diff.min()]
    return min_province[0]
def most_similar_province_pair(data):
    norm_data = data['norm_data']
    province_names = np.array([data["province_names"]])
    norm_data=norm_data.T
    norm_data.resize(len(data['dates']),1,len(data['province_names']))
    diff = ((norm_data - norm_data.swapaxes(1,2))**2).sum(axis=0)
    diff = np.where(province_names==province_names.T,1e9,diff)
    province = np.where(diff==diff.min())
    return(data['province_names'][province[0][0]],data['province_names'][province[1][0]])
def most_similar_in_period(data, province, beg_date, end_date):

    province_index = np.where(data['province_names']==province)
    province_names = np.delete(data['province_names'],province_index,axis = 0)
    province_norm_data = data['norm_data'][province_index]
    norm_data = np.delete(data['norm_data'],province_index,axis = 0)

    st = np.where(data['dates']==beg_date)[0][0]
    ed = np.where(data['dates']==end_date)[0][0]
    province_norm_data = province_norm_data[0][st:ed+1]
    interval = ed-st+1
    indexer = np.array([np.arange(len(data["dates"]) - interval+1)]).T+np.arange(interval)
    all_data = norm_data[: , indexer]
    all_data = (all_data-province_norm_data)**2
    all_data = all_data.sum(axis=2)
    index = np.where(all_data==all_data.min())
    return (province_names[index[0][0]],data['dates'][index[1][0]],data['dates'][index[1][0]+interval-1])

def main():
    # put your own testing codes in this function
    data =  read_data('Assignment\TH_20210401_20210416.csv')
    # data = read_data('Assignment\sample.csv')
    print(most_similar_in_period(data, 'กรุงเทพมหานคร', '2021-04-05', '2021-04-09' ))


    return
main()
