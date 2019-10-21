import pandas as pd
import json
import pickle
import sys
# import numpy


def predict_output(filename):
    data = pd.read_csv(filename)
    loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
    features = ['ndpi_proto_num', 'src2dst_packets', 'src2dst_bytes', 'dst2src_packets', 'dst2src_bytes', 'data_ratio', 'iat_flow_min', 'iat_flow_avg', 'iat_flow_max', 'iat_flow_stddev', 'iat_c_to_s_min', 'iat_c_to_s_avg', 'iat_c_to_s_max', 'iat_c_to_s_stddev',
                'iat_s_to_c_min', 'iat_s_to_c_avg', 'iat_s_to_c_max', 'iat_s_to_c_stddev', 'pktlen_c_to_s_min', 'pktlen_c_to_s_avg', 'pktlen_c_to_s_max', 'pktlen_c_to_s_stddev', 'pktlen_s_to_c_min', 'pktlen_s_to_c_avg', 'pktlen_s_to_c_max', 'pktlen_s_to_c_stddev']
    X = data[features]
    y_pred = loaded_model.predict(X)
    feat = ['src_ip', 'dst_ip', 'ndpi_proto']
    info = data[feat]
    y_pred = pd.DataFrame(y_pred)
    info['predicted'] = y_pred
    # df_ct = pd.concat([info, y_pred])
    return info


# if __name__=='__main__':
#     arguments = sys.argv[1]
#     y=predict_output(arguments)
#     y_list=y.tolist()
#     json_file='predicted.json'
#     json.dump(b, codecs.open(json_file, 'w', encoding='utf-8'), sort_keys=True, indent=4)
