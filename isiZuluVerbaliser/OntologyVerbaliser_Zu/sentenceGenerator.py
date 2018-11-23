from zulurulespw import *

func_dict = {}
func_dict['subclasses'] = isa_zu
func_dict['disjoint'] = nisa_zu
func_dict['exists'] = exists_zu
func_dict['nexist'] = nexist_zu
func_dict['intersection'] = conjunct_zu

func_dict['akhiwe'] = const_a
func_dict['enziwe'] = const_e
func_dict['ingxenye'] = pw
func_dict['ingxenye_s'] = pw_s
func_dict['hlanganyele'] = pw_pi_c
func_dict['umunxa'] = pw_spatial_p
func_dict['isiqephu'] = pw_solid_p

func_dict['aaaa'] = wp
func_dict['bbbb'] = wp_cp
func_dict['cccc'] = wp_s
func_dict['dddd'] = wp_spatial
func_dict['eeee'] = wp_solid_p
func_dict['ffff'] = pw_ci


def evaluate(k, param):
    try:
        return [func_dict[k](param[0], param[1]), None]
    except TypeError:
        try:
            return [func_dict[k](param[0], param[1], param[2]), None]
        except Exception as e:
            return [None, "Error : %s%s" % (func_dict[k].__name__, param)]
