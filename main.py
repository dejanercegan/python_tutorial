import src.ifelse_tut as ifelse_tut
import src.lists_tut as lists_tut
import src.dictionary_tut as dictionary_tut


def main():
    upercase_list = lists_tut.change_to_uppercase(['dejan', 'Branislav'])

    #######################################################################

    input_dict = {
        "Dejan" : "55555",
        "Branislav" : "11111"
    }

    filter_dict = dictionary_tut.filter_dictionary(input_dict, "D")

    #######################################################################

    ifelse_number = ifelse_tut.ifelse_numlist(['11', '4', '-7'])



if __name__ == '__main__':
    main()

