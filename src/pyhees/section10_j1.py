# 家電

import numpy as np
import pandas as pd
import os

from functools import lru_cache

from pyhees.section10_j1_a import get_E_Elc_rfrg_d_t
from pyhees.section10_j1_b import get_E_Elc_tv_led_d_t
from pyhees.section10_j1_c import get_E_Elc_toilet_seat_heater_d_t
from pyhees.section10_j1_d import get_E_Elc_washer_d_t
from pyhees.section10_j1_e import get_E_Elc_kttl_d_t
from pyhees.section10_j1_f import get_E_Elc_microwave_d_t
from pyhees.section10_j1_g import get_E_Elc_rice_cooker_d_t
from pyhees.section10_j1_h import get_E_Elc_PC_d_t
from pyhees.section10_j1_i import get_E_Elc_audio_cd_radio_cassette_d_t
from pyhees.section10_j1_j import get_E_Elc_audio_microsystem_with_md_d_t
from pyhees.section10_j1_k import get_E_Elc_cleaner_d_t
from pyhees.section10_j1_l import get_E_Elc_iron_d_t
from pyhees.section10_j1_m import get_E_Elc_game_d_t
from pyhees.section10_j1_n import get_E_Elc_desk_lamp_d_t
from pyhees.section10_j1_o import get_E_Elc_dryer_d_t


@lru_cache
def load_ap_schedule() -> np.ndarray:
    """家電スケジュールを外部CSVファイルからND配列に読み込む

    Returns
    ----------
    E_Elc_tv_led_d_t : ndarray(N-dimensional array)
        1年間の全時間の家電スケジュールを格納したND配列
        d日t時の家電スケジュールが年開始時から8760個連続して格納されている
    """

    csvpath = os.path.join(os.path.dirname(__file__), 'data', 'HEA_schedule.csv')
    df = pd.read_csv(csvpath, encoding='SHIFT_JIS')
    return df


def get_E_E_AP_ind_p_d_t(p, ExistsTV=False, ExistsToiletSeatHeater=False, ExistsKettle=False, JISYearOfRefrigerator=None, RefrigeratorPower=None, RatedViewTVPower=125.0, RatedStandbyTVPower=0.15, RatedLaundaryPower=None, RatedKettlePower=None, **args) -> np.ndarray:
    """1 時間当たりの居住人数がp人における家電の消費電力量(個々の家電機器を計算する方法)

    Args:
        p (int): 居住人数
        ExistsTV (bool): 液晶テレビの有無. Defaults to False.
        ExistsToiletSeatHeater (bool): 暖房便座の有無. Defaults to False.
        ExistsKettle (bool): 電気ケトルの有無. Defaults to False.
        JISYearOfRefrigerator (str, optional): 冷蔵庫 JIS C 9801の制定・改正年. Defaults to None.
        RefrigeratorPower (float, optional): 冷蔵庫の年間消費電力量[kWh]. Defaults to None.
        RatedViewTVPower (float, optional): 液晶テレビの稼働時の定格消費電力[W]. Defaults to 125.
        RatedStandbyTVPower (float, optional): 液晶テレビの待機時の定格消費電力[W]. Defaults to 0.15.
        RatedLaundaryPower (float, optional): 洗濯機の標準コースの定格消費電力量[Wh]. Defaults to 51.
        RatedKettlePower (float, optional): 電気ケトルの定格消費電力[W]. Defaults to 1160.

    Returns:
        Tuple(np.ndarray*15): 冷蔵庫,液晶テレビ,便座,洗濯機,電気ケトル,電子レンジ,電気炊飯器,パソコン,CDラジカセ,MDコンポ,掃除機,アイロン,ゲーム機,電気スタンド,ヘアドライヤーの1時間ごとの消費電力量[kWh]
    """
    # 冷蔵庫
    if JISYearOfRefrigerator is None or RefrigeratorPower is None:
        E_Elc_rfrg_annual_JIS = 330.0
        JIS_year = 2006
    else:
        E_Elc_rfrg_annual_JIS = RefrigeratorPower
        JIS_year = int(JISYearOfRefrigerator)

    E_Elc_rfrg_d_t = get_E_Elc_rfrg_d_t(
        P_Elc_dfrst_rtd=150,
        C_dfrst=0.9,
        theta_ave_d=np.array([14.6]*365),   #季節に寄らず14.6℃固定になっている
        E_Elc_rfrg_annual_JIS=E_Elc_rfrg_annual_JIS,
        JIS_year=JIS_year
    )

    # スケジュール読込
    df = load_ap_schedule()

    # 液晶テレビ
    if ExistsTV:
        ds1 = df['液晶テレビ（居間）_{}人世帯_待機'.format(p)]
        ds2 = df['液晶テレビ（居間）_{}人世帯_視聴'.format(p)]
        ds3 = df['液晶テレビ（洋室1）_{}人世帯_待機'.format(p)]
        ds4 = df['液晶テレビ（洋室1）_{}人世帯_視聴'.format(p)]
        E_Elc_tv_led_d_t = get_E_Elc_tv_led_d_t(0.15, 125, ds1, ds2, ds3, ds4, p)
    else:
        E_Elc_tv_led_d_t = np.zeros(24*365)

    # 便座
    if ExistsToiletSeatHeater:
        t_toilet_seat_heater_d_t = df['便座_{}人世帯_暖房'.format(p)]
        E_Elc_toilet_seat_heater_d_t = get_E_Elc_toilet_seat_heater_d_t(
            11.23, 45, t_toilet_seat_heater_d_t)
    else:
        E_Elc_toilet_seat_heater_d_t = np.zeros(24*365)

    # 洗濯機
    tm_washer_wash_d_t = df['洗濯機_{}人世帯_洗濯'.format(p)]
    E_Elc_washer_d_t = get_E_Elc_washer_d_t(51, tm_washer_wash_d_t)

    # 電気ケトル
    if ExistsKettle:
        tm_kttl_boil_d_t = df['電気ケトル_{}人世帯_沸上'.format(p)]
        E_Elc_kttl_d_t = get_E_Elc_kttl_d_t(1160, tm_kttl_boil_d_t, p)
    else:
        E_Elc_kttl_d_t = np.zeros(24*365)

    # 電子レンジ
    t_microwave_cook_d_t = df['電子レンジ_{}人世帯_調理'.format(p)]
    E_Elc_microwave_d_t = get_E_Elc_microwave_d_t(1450, t_microwave_cook_d_t)

    # 電気炊飯器
    t_rice_cooker_cook_d_t = df['電気炊飯器_{}人世帯_炊飯'.format(p)]
    t_rice_cooker_keep_d_t = df['電気炊飯器_{}人世帯_保温'.format(p)]
    E_Elc_rice_cooker_d_t = get_E_Elc_rice_cooker_d_t(
        54.19/60, 1210, 2, 15.1, t_rice_cooker_cook_d_t, t_rice_cooker_keep_d_t)

    # パソコン
    ds = df['パソコン_{}人世帯_使用'.format(p)]
    E_Elc_PC_d_t = get_E_Elc_PC_d_t(97, ds)

    # CDラジカセ
    t_audio_cd_radio_cassette_listening_d_t = df['CDラジカセ_{}人世帯_聴取'.format(p)]
    t_audio_cd_radio_cassette_standby_d_t = df['CDラジカセ_{}人世帯_待機'.format(p)]
    E_Elc_audio_cd_radio_cassette_d_t = get_E_Elc_audio_cd_radio_cassette_d_t(
        28, 0.2, t_audio_cd_radio_cassette_listening_d_t, t_audio_cd_radio_cassette_standby_d_t)

    # MDコンポ
    t_audio_microsystem_with_md_listening_d_t = df['MDコンポ_{}人世帯_聴取'.format(
        p)]
    t_audio_microsystem_with_md_standby_d_t = df['MDコンポ_{}人世帯_待機'.format(p)]
    E_Elc_audio_microsystem_with_md_d_t = get_E_Elc_audio_microsystem_with_md_d_t(
        28, 0.2, t_audio_microsystem_with_md_listening_d_t, t_audio_microsystem_with_md_standby_d_t)

    # 掃除機
    t_cleaner_oprt_d_t = df['掃除機_{}人世帯_使用'.format(p)]
    E_Elc_cleaner_d_t = get_E_Elc_cleaner_d_t(1000, t_cleaner_oprt_d_t)

    # アイロン
    t_iron_oprt_d_t = df['アイロン_{}人世帯_使用'.format(p)]
    E_Elc_iron_d_t = get_E_Elc_iron_d_t(1200, t_iron_oprt_d_t)

    # ゲーム
    t_game_standby_d_t = df['PCゲーム機_{}人世帯_待機'.format(p)]
    t_game_play_d_t = df['PCゲーム機_{}人世帯_稼働'.format(p)]
    E_Elc_game_d_t = get_E_Elc_game_d_t(
        0.3, 95.7, t_game_standby_d_t, t_game_play_d_t)

    # スタンド
    t_desk_lamp_oprt_d_t = df['スタンド_{}人世帯_点灯'.format(p)]
    E_Elc_desk_lamp_d_t = get_E_Elc_desk_lamp_d_t(20, t_desk_lamp_oprt_d_t)

    # ヘアドライヤー
    t_dryer_oprt_d_t = df['ヘアドライヤー_{}人世帯_使用'.format(p)]
    E_Elc_dryer_d_t = get_E_Elc_dryer_d_t(1200, t_dryer_oprt_d_t, p)

    return (
        E_Elc_rfrg_d_t,
        E_Elc_tv_led_d_t,
        E_Elc_toilet_seat_heater_d_t,
        E_Elc_washer_d_t,
        E_Elc_kttl_d_t,
        E_Elc_microwave_d_t,
        E_Elc_rice_cooker_d_t,
        E_Elc_PC_d_t,
        E_Elc_audio_cd_radio_cassette_d_t,
        E_Elc_audio_microsystem_with_md_d_t,
        E_Elc_cleaner_d_t,
        E_Elc_iron_d_t,
        E_Elc_game_d_t,
        E_Elc_desk_lamp_d_t,
        E_Elc_dryer_d_t
    )



if __name__ == '__main__':
    p = 4

    E_Elc = get_E_E_AP_ind_p_d_t(p)

    E_Elc_rfrg_d_t, \
    E_Elc_tv_led_d_t, \
    E_Elc_toilet_seat_heater_d_t, \
    E_Elc_washer_d_t, \
    E_Elc_kttl_d_t, \
    E_Elc_microwave_d_t, \
    E_Elc_rice_cooker_d_t, \
    E_Elc_PC_d_t, \
    E_Elc_audio_cd_radio_cassette_d_t, \
    E_Elc_audio_microsystem_with_md_d_t, \
    E_Elc_cleaner_d_t, \
    E_Elc_iron_d_t, \
    E_Elc_game_d_t, \
    E_Elc_desk_lamp_d_t, \
    E_Elc_dryer_d_t = E_Elc

    # 冷蔵庫
    print('E_Elc_rfrg: {} kWh/year'.format(sum(E_Elc_rfrg_d_t)))

    # 液晶テレビ
    print('E_Elc_tv_led: {} kWh/year'.format(sum(E_Elc_tv_led_d_t)))

    # 便座
    print('E_Elc_toilet_seat_heater: {} kWh/year'.format(sum(E_Elc_toilet_seat_heater_d_t)))

    # 洗濯機
    print('E_Elc_washer: {} kWh/year'.format(sum(E_Elc_washer_d_t)))

    # 電気ケトル
    print('E_Elc_kttl: {} kWh/year'.format(sum(E_Elc_kttl_d_t)))

    # 電子レンジ
    print('E_Elc_microwave: {} kWh/year'.format(sum(E_Elc_microwave_d_t)))

    # 電気炊飯器
    print('E_Elc_rice_cooker: {} kWh/year'.format(sum(E_Elc_rice_cooker_d_t)))

    # パソコン
    print('E_Elc_PC: {} kWh/year'.format(sum(E_Elc_PC_d_t)))

    # CDラジカセ
    print('E_Elc_audio_cd_radio_cassette: {} kWh/year'.format(sum(E_Elc_audio_cd_radio_cassette_d_t)))

    # MDコンポ
    print('E_Elc_audio_microsystem_with_md: {} kWh/year'.format(sum(E_Elc_audio_microsystem_with_md_d_t)))

    # 掃除機
    print('E_Elc_cleaner: {} kWh/year'.format(sum(E_Elc_cleaner_d_t)))

    # アイロン
    print('E_Elc_iron: {} kWh/year'.format(sum(E_Elc_iron_d_t)))

    # ゲーム
    print('E_Elc_game: {} kWh/year'.format(sum(E_Elc_game_d_t)))

    # スタンド
    print('E_Elc_desk_lamp: {} kWh/year'.format(sum(E_Elc_desk_lamp_d_t)))

    # ヘアドライヤー
    print('E_Elc_dryer: {} kWh/year'.format(sum(E_Elc_dryer_d_t)))
