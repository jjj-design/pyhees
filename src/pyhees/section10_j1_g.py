# 電気炊飯器

def get_E_Elc_rice_cooker_d_t(t_rice_cooker_cook, P_Elc_rice_cooker_rtd, N_cup_of_rice, E_Elc_rice_cooker_keep, t_rice_cooker_cook_d_t, t_rice_cooker_keep_d_t):
    """時刻別消費電力量を計算する

    Parameters
    ----------
    t_rice_cooker_cook : float
        炊飯1回当たりの時間(54.19/60), h

    P_Elc_rice_cooker_rtd : float
        定格消費電力, W

    N_cup_of_rice : float
        炊飯号数, 合

    E_Elc_rice_cooker_keep : float
        保温時の消費電力量, Wh

    t_rice_cooker_cook_d_t : ndarray(N-dimensional array)
        1年間の全時間の炊飯時間を格納したND配列, h
        d日t時の炊飯時間が年開始時から8760個連続して格納されている

    t_rice_cooker_keep_d_t : ndarray(N-dimensional array)
        1年間の全時間の保温時間を格納したND配列, h
        d日t時の保温時間が年開始時から8760個連続して格納されている

    Returns
    ----------
    E_Elc_rice_cooker_d_t : ndarray(N-dimensional array)
        1年間の全時間の消費電力量を格納したND配列, Wh
        d日t時の消費電力量が年開始時から8760個連続して格納されている
    """

    P_Elc_rice_cooker_cook = get_P_Elc_rice_cooker_cook(
        t_rice_cooker_cook, P_Elc_rice_cooker_rtd, N_cup_of_rice)
    P_Elc_rice_cooker_keep = get_P_Elc_rice_cooker_keep(E_Elc_rice_cooker_keep)

    E_Elc_rice_cooker_d_t = P_Elc_rice_cooker_cook * t_rice_cooker_cook_d_t \
        + P_Elc_rice_cooker_keep * t_rice_cooker_keep_d_t

    E_Elc_rice_cooker_d_t = E_Elc_rice_cooker_d_t * 10**(-3)

    return E_Elc_rice_cooker_d_t


def get_P_Elc_rice_cooker_cook(t_rice_cooker_cook, P_Elc_rice_cooker_rtd, N_cup_of_rice):
    """炊飯時の消費電力を計算する

    Parameters
    ----------
    t_rice_cooker_cook : float
        炊飯1回当たりの時間(54.19/60), h

    P_Elc_rice_cooker_rtd : float
        定格消費電力, W

    N_cup_of_rice : float
        炊飯号数, 合

    Returns
    ----------
    P_Elc_rice_cooker_cook  : float
        炊飯時の消費電力, W
    """

    '''
    E_Elc_rice_cooker_cook = 0.029 * P_Elc_rice_cooker_rtd \
                           + ( 32.414 * N_cup_of_rice + 58.745)
    
    # /試算結果_家電の電力消費量.xlsx　に合わせるための処理
    t_rice_cooker_cook = 143.30775 * 60 / E_Elc_rice_cooker_cook
    t_rice_cooker_cook = t_rice_cooker_cook / 60
    P_Elc_rice_cooker_cook = E_Elc_rice_cooker_cook * t_rice_cooker_cook
    # 試算結果_家電の電力消費量.xlsx　に合わせるための処理/    
    
    '''

    P_Elc_rice_cooker_cook = 143.30775

    return P_Elc_rice_cooker_cook


def get_P_Elc_rice_cooker_keep(E_Elc_rice_cooker_keep):
    """保温時の消費電力を計算する

    Parameters
    ----------
    E_Elc_rice_cooker_keep : float
        保温時の消費電力量, Wh

    Returns
    ----------
    P_Elc_rice_cooker_keep : float
        保温時の消費電力, W
    """

    P_Elc_rice_cooker_keep = E_Elc_rice_cooker_keep / 1

    return P_Elc_rice_cooker_keep
