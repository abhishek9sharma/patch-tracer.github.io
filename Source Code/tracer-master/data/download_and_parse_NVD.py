# -*- coding: utf-8 -*-

"""
Created on 2020-04-04 13:57  


CVE-2014-2925 Pass, to check,  len(tr[class]) == 0  !
CVE-2011-0395 Pass, to check,  len(tr[class]) == 0  !
CVE-2014-1902 Pass, to check,  len(tr[class]) == 0  !

CVE-2019-12220 ['AND']
CVE-2004-1416 ['OR']
CVE-2010-1802 ['AND', 'OR', 'OR']
"""

import os
import urllib
from bs4 import BeautifulSoup
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
sys.path.append('../../')
sys.path.append('../../..')
import urllib.parse
import logging
import gzip

from vulnerability_analysis import config
from vulnerability_analysis.utility import json_processing, item_template, file_processing, log
from vulnerability_analysis.utility.crawler import crawl_util
# from vulnerability_analysis.DR008_present_CVE_metadata.auto_update_nvd_dataset import download_and_parse_NVD_cpe_ranges

l1_split_str = config.L1_SPLITE_STR
l2_split_str = config.L2_SPLITE_STR
cve_dataset_path = config.CVE_DATASET_PATH
NVD_dataset_path = config.NVD_DATASET_DIR
NVD_dataset_items_dir = config.NVD_DATASET_ITEMS_DIR
NVD_CPErange_items_dir = config.NVD_CPERANGE_ITEMS_DIR
DR008_presented_metadata_field_list = config.DR008_PRESENTED_METADTA_LIST
logger = log.create_logger(level = logging.INFO, log_file_path = config.LOG_DR008_DOWNLOAD_AND_PARSE_NVD, logger_name = 'download_and_parse_NVD', print_stream_cmd=True)
log_content = file_processing.read_TXTfile(config.LOG_DR008_DOWNLOAD_AND_PARSE_NVD)



def download_NVD_data_feed():
    for year in range(2017,2018):
        logger.info('download_NVD_data_feed(): ' + year.__str__())
        url = 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-%s.json.gz' % str(year)
        file_path = NVD_dataset_path + 'nvdcve-1.1-%s.json.gz' % str(year)
        crawl_util.save_file_from_url_cover_existing(url=url, path=file_path )
        # 获取文件的名称，去掉后缀名
        f_name = file_path.replace(".gz", "")
        # 开始解压
        g_file = gzip.GzipFile(file_path)
        # 读取解压后的文件，并写入去掉后缀名的同名文件（即得到解压后的文件）
        open(f_name, "wb+").write(g_file.read())

def separateCVEItems():
    # tongji
    count_update = 0
    count_add = 0
    for year in range(2017,2018):
        file_path = NVD_dataset_path + "nvdcve-1.1-" + str(year) +'.json'
        year_dataset_content = json_processing.read(file_path)

        # separate:
        CVE_Items = year_dataset_content['CVE_Items']
        for CVE_Item in CVE_Items:
            CVEID = CVE_Item['cve']['CVE_data_meta']['ID']
            path = NVD_dataset_items_dir + CVEID +'.json'
            res = update_CVE_item(CVEID=CVEID, CVE_Item_data=CVE_Item)
            json_processing.write(json_content=CVE_Item, path=path)

            if res == 1:
                count_add +=1
            elif res == 2:
                count_update +=1
        print(year,'count_update', count_update, 'count_add', count_add)
    print('count_update',count_update,'count_add',count_add)

def update_CVE_item(CVEID , CVE_Item_data):
    """
    根据modified date，判断是否需要更新
    :param CVEID:
    :param CVE_Item_data:
    :return:
    """
    CVE_item_path = NVD_dataset_items_dir + CVEID +'.json'
    if not file_processing.pathExist( CVE_item_path ):
        return 1 # add
    elif not json_processing.read(CVE_item_path):
        return 1  # add
    else:
        # 判断是否相同
        existing_item_update_date = json_processing.read(CVE_item_path)['lastModifiedDate']
        new_item_update_date = CVE_Item_data['lastModifiedDate']
        if existing_item_update_date != new_item_update_date:
            # update
            print('update： ',CVEID,existing_item_update_date, new_item_update_date)
            # download_and_parse_NVD_cpe_ranges.crawl_and_parse_CVECpeRange(CVEID=CVEID, cover_switch=True)
            return 2  # update

def main():
    logger.info('start')
    download_NVD_data_feed()
    logger.info('finish download_NVD_data_feed()')
    separateCVEItems()  # 从导出的NVD feed中数据，将每个NVD信息分割开
    logger.info('finish separateCVEItems()')

if __name__ == '__main__':
    main()

