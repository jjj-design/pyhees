import numpy as np

# 冷蔵庫


def get_E_Elc_rfrg_d_t(P_Elc_dfrst_rtd, C_dfrst, theta_ave_d, E_Elc_rfrg_annual_JIS, JIS_year):
    """時刻別消費電力量を計算する

    Parameters
    ----------
    P_Elc_dfrst_rtd : float
        除霜用電熱装置の定格消費電力( = 150 ), W

    C_dfrst : float
        除霜用電熱装置の消費電力量の評価係数( = 0.9 ), -

    theta_ave_d : ndarray(N-dimensional array)
        日別の平均外気温度を格納したND配列, ℃
        d日の平均外気温度が年開始日から365個連続して格納されている

    E_Elc_rfrg_annual_JIS : float
        JISに準拠して測定された年間消費電量, kWh

    JIS_year : Int
        年間消費電力量の測定時に準拠したJIS規格の制定・改正年, 年

    Returns
    ----------
    E_Elc_rfrg_d_t : ndarray(N-dimensional array)
        1年間の全時間の消費電力量を格納したND配列, Wh
        d日t時の消費電力量が年開始時から8760個連続して格納されている
    """

    theta_amb_ave_d = get_theta_amb_ave_d(theta_ave_d)
    E_Elc_rfrg_annual = get_E_Elc_rfrg_annual(E_Elc_rfrg_annual_JIS, JIS_year)
    P_Elc_rfrg_oprt_ave_d = get_P_Elc_rfrg_oprt_ave_d(
        E_Elc_rfrg_annual, theta_amb_ave_d, P_Elc_dfrst_rtd, C_dfrst)

    rfrg_dfrst_d = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    rfrg_oprt_d = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

    rfrg_dfrst_d_t = np.tile(rfrg_dfrst_d, 365)
    rfrg_oprt_d_t = np.tile(rfrg_oprt_d, 365)

    E_Elc_rfrg_dfrst_d_t = rfrg_dfrst_d_t * \
        P_Elc_dfrst_rtd * C_dfrst * 1 * 10**(-3)
    P_Elc_rfrg_oprt_ave_d_t = np.array([])
    for p in P_Elc_rfrg_oprt_ave_d:
        P_Elc_rfrg_oprt_ave_d_t = np.append(
            P_Elc_rfrg_oprt_ave_d_t, np.tile(p, 24))
    E_Elc_rfrg_oprt_d_t = rfrg_oprt_d_t * \
        P_Elc_rfrg_oprt_ave_d_t * 1 * 10**(-3)

    E_Elc_rfrg_d_t = E_Elc_rfrg_dfrst_d_t + E_Elc_rfrg_oprt_d_t

    return E_Elc_rfrg_d_t


def get_P_Elc_rfrg_oprt_ave_d(E_Elc_rfrg_annual, theta_amb_ave_d, P_Elc_dfrst_rtd, C_dfrst):
    """
    Parameters
    ----------
    E_Elc_rfrg_annual : float
        年間消費電量, kWh

    theta_amb_d : ndarray(N-dimensional array)
        1年間の冷蔵庫の周辺空気の日平均温度を格納したND配列, ℃
        d日の冷蔵庫の周辺空気の日平均温度が年開始時から365個連続して格納されている

    P_Elc_dfrst_rtd : float
        除霜用電熱装置の定格消費電力( = 150 ), W

    C_dfrst : float
        除霜用電熱装置の消費電力量の評価係数( = 0.9 ), -

    Returns
    ----------
    P_Elc_rfrg_oprt_ave_d : ndarray(N-dimensional array)
        1年間の稼働時の平均消費電力を格納したND配列, W
        d日の稼働時の平均消費電力が年開始時から365個連続して格納されている
    """

    P_Elc_rfrg_est_d = \
        (
            (3.283 * 10**(-3) - 2.0 * 10**(-6) * E_Elc_rfrg_annual)
            * (theta_amb_ave_d**2 - 30 * theta_amb_ave_d)
            + 1.85 * 10**(-3) * E_Elc_rfrg_annual
            + 1.329
        ) * 10**3

    P_Elc_rfrg_oprt_ave_d = (
        P_Elc_rfrg_est_d - (P_Elc_dfrst_rtd * C_dfrst) * 2) / 22

    return P_Elc_rfrg_oprt_ave_d


def get_theta_amb_ave_d(theta_ave_d):
    """時刻別消費電力量を計算する

    Parameters
    ----------
    theta_ave_d : ndarray(N-dimensional array)
        1年間の外気の日平均温度[℃]を格納したND配列
        d日の外気の日平均温度(＝14.6通年で一定値)[℃]が年開始時から365個連続して格納されている

    Returns
    ----------
    theta_amb_d : ndarray(N-dimensional array)
        1年間の冷蔵庫の周辺空気の日平均温度[℃]を格納したND配列
        d日の冷蔵庫の周辺空気の日平均温度[℃]が年開始時から365個連続して格納されている
    """

    theta_amb_ave_d = 0.4142 * theta_ave_d + 15.47

    return theta_amb_ave_d


def get_E_Elc_rfrg_annual(E_Elc_rfrg_annual_JIS, JIS_year):
    """時刻別消費電力量を計算する

    Parameters
    ----------
    E_Elc_rfrg_annual_JIS : float
        JISに準拠して測定された年間消費電量[kWh]

    JIS_year : Int
        年間消費電力量の測定時に準拠したJIS規格の制定年[年]

    Returns
    ----------
    E_Elc_rfrg_annual : float
        年間消費電量[kWh]
    """

    if JIS_year == 1999:
        E_Elc_rfrg_annual = E_Elc_rfrg_annual_JIS
    elif JIS_year == 2006:
        E_Elc_rfrg_annual = E_Elc_rfrg_annual_JIS / 3.48
    elif JIS_year == 2015:
        E_Elc_rfrg_annual = E_Elc_rfrg_annual_JIS / 3.48 * 0.2891
    else:
        raise ValueError(JIS_year)

    return E_Elc_rfrg_annual
