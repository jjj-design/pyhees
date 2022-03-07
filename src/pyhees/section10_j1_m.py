# PCゲーム機

def get_E_Elc_game_d_t(P_Elc_game_standby_measured, P_Elc_game_play_measured, t_game_standby_d_t, t_game_play_d_t):
    """時刻別消費電力量を計算する
    
    Parameters
    ----------
    P_Elc_game_standby_measured : float
        待機時の消費電力の実測値, W
        
    P_Elc_game_play_measured : float
        稼働時の消費電力の実測値, W
        
    t_game_standby_d_t : ndarray(N-dimensional array)
        1年間の全時間の待機時間を格納したND配列, h
        d日t時の待機時間が年開始時から8760個連続して格納されている
    
    t_game_play_d_t : ndarray(N-dimensional array)
        1年間の全時間の稼働時間を格納したND配列, h
        d日t時の稼働時間が年開始時から8760個連続して格納されている

    Returns
    ----------
    E_Elc_game_d_t : ndarray(N-dimensional array)
        1年間の全時間の消費電力量を格納したND配列, Wh
        d日t時の消費電力量が年開始時から8760個連続して格納されている
    """
    
    P_Elc_game_standby = get_P_Elc_game_standby(P_Elc_game_standby_measured)
    P_Elc_game_play = get_P_Elc_game_play(P_Elc_game_play_measured)

    E_Elc_game_d_t \
        = P_Elc_game_standby * t_game_standby_d_t \
        + P_Elc_game_play * t_game_play_d_t
        
    E_Elc_game_d_t = E_Elc_game_d_t * 10**(-3)
    
    return E_Elc_game_d_t



def get_P_Elc_game_standby(P_Elc_game_standby_measured):
    """待機時の消費電力を計算する
    
    Parameters
    ----------
    P_Elc_game_standby_measured : float
        待機時の平均消費電力（実測値）, W

    Returns
    ----------
    P_Elc_game_standby : float
        稼働時消費電力, W
    """
        
    P_Elc_game_standby = P_Elc_game_standby_measured
        
    return P_Elc_game_standby



def get_P_Elc_game_play(P_Elc_game_play_measured):
    """稼働時の消費電力を計算する
    
    Parameters
    ----------
    P_Elc_game_play_measured : float
        稼働時の平均消費電力（実測値）, W

    Returns
    ----------
    P_Elc_game_play : float
        稼働時消費電力, W
    """
        
    P_Elc_game_play = P_Elc_game_play_measured
        
    return P_Elc_game_play

    