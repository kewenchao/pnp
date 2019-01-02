#!/usr/bin/env python
# !coding=utf8

import json
import logging
import requests
import time

logger = logging.getLogger(__name__)

AIA_Latest = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'KBL-NUC',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A N MR1',
    'test_mode': 'Latest',
    'project_name': 'Android IA',
    'cmdmode': 'true',
    'cases': json.dumps(["Perf_Total_AIA_Latest"])
}

AIA_WeeklyRC = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'KBL-NUC',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A O MR1',
    'test_mode': 'Weekly-RC',
    'project_name': 'Android IA',
    'cmdmode': 'true',
    'cti_device_id': '90',
    'trigger_by_device_id': 'true',
    #'cases': json.dumps(["Perf_Total_AIA_Weekly_RC", "Power_Total_AIA_Weekly_RC","Perf_Total_AIA_labjack_Weekly_RC"])
    'cases': json.dumps(["Perf_Total_AIA_Weekly_RC"])
}

Celadon_KBL_IVI_WeeklyRC = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'KBL-IVI UI',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'N',
    'flash_image_url': '',
    'distro': '1A O MR1',
    'test_mode': 'Weekly-RC',
    'project_name': 'Celadon',
    'cmdmode': 'true',
    'cti_device_id': '128',
    'trigger_by_device_id': 'true',
    'cases': json.dumps(["Perf_Total_Celadon_Weekly_RC"])
}

Celadon_KBL_TABLET_WeeklyRC = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'KBL-NUC Tablet',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'N',
    'flash_image_url': '',
    'distro': '1A O MR1',
    'test_mode': 'Weekly-RC',
    'project_name': 'Celadon',
    'cmdmode': 'true',
    'cti_device_id': '90',
    'trigger_by_device_id': 'true',
    'cases': json.dumps(["Perf_Total_Celadon_Weekly_RC"])
}
AIA_Daily = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'KBL-NUC',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A N MR1',
    'test_mode': 'Daily',
    'project_name': 'Android IA',
    'cmdmode': 'true',
    'cases': json.dumps(["Perf_Total_AIA_Daily", "Power_Total_AIA_Daily"])
}

BXT_Daily_O = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'BXTP IVI MRB 8G',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A O MR0',
    'test_mode': 'Daily',
    'project_name': 'Android',
    'cmdmode': 'true',
    'cases': json.dumps(["Perf_Total_BXT_O_Kernel"])
}

BXT_Daily_O_MR1 = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'BXTP IVI MRB 8G',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A O MR1',
    'test_mode': 'Daily',
    'project_name': 'Android',
    'cmdmode': 'true',
    'cases': json.dumps(["Perf_Total_BXT_O_MR1_Daily","Perf_Total_BXT_O_MR1_labjack"])
}
BXT_Daily_P_MR0 = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'BXTP IVI MRB 8G',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A P MR0',
    'test_mode': 'Daily',
    'project_name': 'Android',
    'cmdmode': 'true',
    'cti_device_id': '81',
    'cases': json.dumps(["Perf_Total_BXT_P_MR0_Daily","Perf_Total_BXT_P_MR0_Daily_labjack"])
}

BXT_Daily_O_MR1_4G = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'BXTP IVI MRB 4G',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A O MR1',
    'test_mode': 'Daily',
    'project_name': 'Android',
    'cmdmode': 'true',
    'cases': json.dumps(["Perf_Total_BXT_O_MR1_4G_Daily"])
}

BXT_Daily_P_MR0_4G = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'BXTP IVI MRB 4G',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A P MR0',
    'test_mode': 'Daily',
    'project_name': 'Android',
    'cmdmode': 'true',
    'cases': json.dumps(["Perf_Total_BXT_P_MR0_Daily_4G"])
}

BXT_Latest_O_MR1 = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'BXTP IVI MRB B1 8G',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A O MR1',
    'test_mode': 'Latest',
    'project_name': 'Android',
    'cmdmode': 'true',
    'cti_device_id': '37',
    'trigger_by_device_id': 'true',
    'cases': json.dumps(["Perf_Total_BXT_O_MR1_Latest"])
}

BXT_Latest_P_MR0 = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'BXTP IVI MRB 8G',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A P MR0',
    'test_mode': 'Latest',
    'project_name': 'Android',
    'cmdmode': 'true',
    'cti_device_id': '81',
    'trigger_by_device_id': 'true',
    'cases': json.dumps(["Perf_Total_BXT_P_MR0_Latest"])
}

BXT_WeeklyRC_O_MR1 = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'BXTP IVI B1 8G',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A O MR1',
    'test_mode': 'Weekly-RC',
    'project_name': 'Android',
    'cmdmode': 'true',
    'cases': json.dumps(["Perf_Total_BXT_O_MR1_WeeklyRC"])
}

BXT_PST_P_MR0 = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'BXTP IVI MRB 8G',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A P MR0',
    'test_mode': 'PST',
    'project_name': 'Android',
    'cmdmode': 'true',
    'cti_device_id': '81',
    'cases': json.dumps(["Perf_Total_BXT_P_MR0_PST","Perf_Total_BXT_P_MR0_PST_UX"])
}

BXT_WeeklyRC_P_MR0 = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'BXTP IVI MRB 8G',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A P MR0',
    'test_mode': 'Weekly-RC',
    'project_name': 'Android',
    'cmdmode': 'true',
    'cti_device_id': '81',
    'cases': json.dumps(["Perf_Total_BXT_P_MR0_Weekly_RC","Perf_Total_BXT_P_MR0_Daily_labjack"])
}

BXT_Daily_P_ACRN = {
    'user_name': 'qianchex',
    'password': 'hector_234',
    'metrix_device_name': 'BXTP IVI MRB 8G',
    'compare_image': '',
    'build_name': '',
    'build_number': '',
    'emails': 'qianx.a.chen@intel.com',
    'metrix_report': 'Y',
    'flash_image_url': '',
    'distro': '1A P ACRN',
    'test_mode': 'Daily',
    'project_name': 'Android',
    'cmdmode': 'true',
    'cti_device_id': '140',
    'trigger_by_device_id': 'true',
    'cases': json.dumps(["Perf_Total_BXT_P_ACRN_Daily"])
}

CI_METRIX_BUILD_MAP = {
    'latest': 'Latest',
    'upload-daily-branch': 'Daily',
    'release_candidate': 'Weekly-RC',
    'release': 'Weekly',
    'preintegration': 'PST',
}

proxies = {
    'http': 'http://child-prc.intel.com:913',
    'https': 'http://child-prc.intel.com:913',
}

# api_url = 'http://pnp.sh.intel.com/ats_cti/api/sessions'
# api_url = 'http://pnp.sh.intel.com/cpats/api/sessions_cmd'
#api_url = 'http://pnp.sh.intel.com/PnPTaaS/api/sessions_cmd'
api_url = 'http://pnp-taas.intel.com/api/sessions'
#api_url = 'http://pnp-taas-dev.sh.intel.com/api/sessions_cmd'



def submit_session(**job_params):
    status = True
    message = "success"
    data = {}
    data2 = {}
    artOutputURL = job_params.get('artOutputURL')
    image_name = "{}-flashfiles-{}.zip".format(job_params.get('target_product'),
                                               job_params.get('short_build_number'))
    #build_name = "[{}]{}".format(CI_METRIX_BUILD_MAP.get(job_params.get('buildvariant')), image_name)

    job_image_url = "{}{}/userdebug/{}".format(artOutputURL,
                                               job_params.get('target_product'),
                                               image_name)
    #build_name = job_image_url
    build_name = "[{}]{}".format(CI_METRIX_BUILD_MAP.get(job_params.get('buildvariant')), job_image_url)
    build_number = '{}_{}'.format(time.strftime("%Y%m%d", time.localtime()),
                                  artOutputURL.split('/')[-2])

    if job_params.get('target_product') == 'androidia_64' and job_params.get('buildvariant') == 'latest':
        data = AIA_Latest
    elif job_params.get('target_product') == 'androidia_64' and \
            job_params.get('buildvariant') == 'release_candidate':
        data = AIA_WeeklyRC
    elif job_params.get('target_product') == 'cel_apl' and \
            job_params.get('buildvariant') == 'release_candidate':
        data = Celadon_KBL_IVI_WeeklyRC
    elif job_params.get('target_product') == 'celadon' and \
            job_params.get('buildvariant') == 'release_candidate':
        data = Celadon_KBL_TABLET_WeeklyRC
    elif job_params.get('target_product') == 'androidia_64' and \
            job_params.get('buildvariant') == 'upload-daily-branch':
        data = AIA_Daily
        build_number = artOutputURL.split('/')[-2]
    elif job_params.get('target_product') == 'gordon_peak' and job_params.get(
            'buildvariant') == 'upload-daily-branch' and job_params.get('manifest_branch') == 'android/o/mr0/master':
        data = BXT_Daily_O
        build_number = artOutputURL.split('/')[-2]
    elif job_params.get('target_product') == 'gordon_peak' and job_params.get(
            'buildvariant') == 'upload-daily-branch' and job_params.get('manifest_branch') == 'android/p/mr0/stable/bxtp_ivi/master':
        data = BXT_Daily_P_MR0
        build_number = artOutputURL.split('/')[-2]
    elif job_params.get('target_product') == 'gordon_peak' and job_params.get(
            'buildvariant') == 'preintegration' and job_params.get('manifest_branch') == 'android/p/mr0/stable/bxtp_ivi/master':
        data = BXT_PST_P_MR0
        build_number = artOutputURL.split('/')[-2]
    elif job_params.get('target_product') == 'gordon_peak' and job_params.get('buildvariant') == 'release_candidate' \
            and job_params.get('manifest_branch') == 'android/p/mr0/stable/bxtp_ivi/master':
        data = BXT_WeeklyRC_P_MR0
    elif job_params.get('target_product') == 'gordon_peak_acrn' and job_params.get(
            'buildvariant') == 'upload-daily-branch' and job_params.get('manifest_branch') == 'android/master':
        data = BXT_Daily_P_ACRN
        build_number = artOutputURL.split('/')[-2]
    else:
        status = "3"
        message = "Not in PnP automation test plan, exit!"
        return status, message

    if data:
        if job_image_url and job_image_url.endswith('.zip'):
            data['flash_image_url'] = job_image_url
        else:
            status = False
            message = "Flash URL is not right!"
            return status, message
        if build_name:
            data['build_name'] = build_name
        else:
            status = False
            message = "No Build name!"
            return status, message
        if build_number:
            data['build_number'] = build_number
        else:
            status = False
            message = "No Build number!"
            return status, message
    else:
        status = False
        message = "No Data!"
        return status, message

    if data2:
        if job_image_url and job_image_url.endswith('.zip'):
            data2['flash_image_url'] = job_image_url
        else:
            status = False
            message = "Flash URL is not right!"
            return status, message
        if build_name:
            data2['build_name'] = build_name
        else:
            status = False
            message = "No Build name!"
            return status, message
        if build_number:
            data2['build_number'] = build_number
        else:
            status = False
            message = "No Build number!"
            return status, message
    #print 'data=%s' % data
    #print 'data2=%s' % data2
    resp = requests.post(api_url, data=data, proxies=proxies)
    time.sleep(1)
    print resp.status_code
    print resp.content
    if data2:
        resp = requests.post(api_url, data=data2, proxies=proxies)
        time.sleep(1)
        print resp.status_code
        print resp.content
    #return json.loads(resp.content).get('message').split('Session_id:')[-1]
    return status, message


def submit_sessions(**job_params):
    return submit_session(**job_params)
