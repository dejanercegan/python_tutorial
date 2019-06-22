import src.ifelse_tut as ifelse_tut
import src.lists_tut as lists_tut
import src.dictionary_tut as dictionary_tut
import src.forwhile_tut as forwhile_tut


def main():
    upercase_list = lists_tut.change_to_uppercase(['dejan', 'Branislav'])

    #######################################################################

    input_dict = {
        "Dejan" : "55555",
        "Branislav" : "11111"
    }

    filter_dict = dictionary_tut.filter_dictionary(input_dict, "D")

    #######################################################################

    ifelse_number = ifelse_tut.ifelse_numlist(['-99', '46', '5'])

    #######################################################################

    firwhile_myname = forwhile_tut.forwhile_names(['Dejan', 'Srdjan', 'Branislav'])



if __name__ == '__main__':
    main()

