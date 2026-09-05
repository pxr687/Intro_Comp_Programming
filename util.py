# Random array entries.
import numpy as np

def mk_t_1():
    rndm = np.array([-1*10*(100 * 22)/10*-1, "3S5I!AyM_ HUJN_I*V^E=RRSyIYTUYP"[1::2] ,
                      (27*1000) + (1000/27) - (27*1000),
                    "fTthyiusi iioso oat rfeiwnaez aacnvsbwyetrw"[1::2],
                      999 * 3 + (100*100*2) - 999 * 3])
    return rndm

def mk_t_2():
    rndm = np.array([(2**10) + (100 ** 2) - (2**10),
                    (1245 * 2) + (8 * 4 / 2) - (1245 * 2),
                    (9 * 34) + (2 ** 2 * (4 + 6)) - (9 * 34),
                    (8 * 9 * 10) + ((8 - 6) * 2 + 24) - (8 * 9 * 10),
                    (25 * 4) * (9 * 4 + 8 / (2 - 3)) / (4 * 25)])
    return rndm

def mk_t_2a():
    # Gen obs for Git.
    obs_1 = "b3!rr".join("arc5!!!").join("_4d").join("98")[(2 ** 5) // (3 * 5 + 1)]
    obs_2 = "43!rr".join("bra_890").join("_c").join("97")[(2 ** 5) // (3 * 5 + 1)]
    obs_3 = "93!rr".join("crd3!___").join("_b").join("9f")[(2 ** 5) // (3 * 5 + 1)]
    obs_4 = "43!rr".join("dra3nnn").join("_kc").join("97")[(2 ** 5) // (3 * 5 + 1)]
    return obs_1, obs_2, obs_3, obs_4