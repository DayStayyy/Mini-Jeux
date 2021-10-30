#!/bin/bash

function printArray() {
    array=$1

    echo " |-1-2-3-|"
    echo -e "A| ${array[1]} ${array[2]} ${array[3]} |"
    echo -e "B| ${array[4]} ${array[5]} ${array[6]} |"
    echo -e "C| ${array[7]} ${array[8]} ${array[9]} |"
    echo " |-------|"
}

function checkGameStatus() {
    if [ $? -ne 0 ]
    then
        echo "ERROR : NO OR TOO MUCH PARAMETERS IN CHECKGAMESTATUS"
    else
        array=$1
        if [ "${array[1]}" != " " ]
        then
            if [ "${array[1]}" == "${array[2]}" ] & [ "${array[1]}" == "${array[3]}" ]
            then
                GAME=${array[1]}
            elif [ "${array[1]}" == "${array[4]}" ] & [ "${array[1]}" == "${array[7]}" ]
            then
                GAME=${array[1]}
            elif [ "${array[1]}" == "${array[5]}" ] & [ "${array[1]}" == "${array[8]}" ]
            then
                GAME=${array[1]}
            fi
        elif [ "${array[9]}" != " " ]
        then
            if [ "${array[9]}" == "${array[6]}" ] & [ "${array[9]}" == "${array[3]}" ]
            then
                GAME=${array[1]}
            elif [ "${array[9]}" == "${array[8]}" ] & [ "${array[9]}" == "${array[7]}" ]
            then
                GAME=${array[1]}
            fi
        elif [ "${array[5]}" != " " ]
        then
            echo "YO"
            if [ "${array[5]}" == "${array[4]}" ] & [ "${array[5]}" == "${array[6]}" ]
            then
                GAME=${array[1]}
            elif [ "${array[5]}" == "${array[2]}" ] & [ "${array[5]}" == "${array[8]}" ]
            then
                echo "YO2"
                GAME=${array[1]}
            elif [ "${array[5]}" == "${array[7]}" ] & [ "${array[5]}" == "${array[3]}" ]
            then
                GAME=${array[1]}
            fi
        fi
    fi
}

function askPlay() {
    read -p "$1, Entrez la case dans laquelle vous voulez jouer(Ex: A2) : " $2
    return $2 2>/dev/null
}

function caseToIndex() {
    if [ "$1" == "A1" ]
    then
       RESULT=1
    fi
    if [ "$1" == "A2" ]
    then
        RESULT=2
    fi
    if [ "$1" == "A3" ]
    then
       RESULT=3
    fi
    
    # 2ème ligne
    if [ "$1" == "B1" ]
    then
        RESULT=4
    fi
    if [ "$1" == "B2" ]
    then
        RESULT=5
    fi
    if [ "$1" == "B3" ]
    then
        RESULT=6
    fi

    # 3ème ligne
    if [ "$1" == "C1" ]
    then
        RESULT=7
    fi
    if [ "$1" == "C2" ]
    then
        RESULT=8
    fi
    if [ "$1" == "C3" ]
    then
        RESULT=9
    fi

    # 1ère ligne
    if [ "$1" == "a1" ]
    then
        RESULT=1
    fi
    if [ "$1" == "a2" ]
    then
        RESULT=2
    fi
    if [ "$1" == "a3" ]
    then
       RESULT=3
    fi
    
    # 2ème ligne
    if [ "$1" == "b1" ]
    then
        RESULT=4
    fi
    if [ "$1" == "b2" ]
    then
        RESULT=5
    fi
    if [ "$1" == "b3" ]
    then
        RESULT=6
    fi

    # 3ème ligne
    if [ "$1" == "c1" ]
    then
        RESULT=7
    fi
    if [ "$1" == "c2" ]
    then
        RESULT=8
    fi
    if [ "$1" == "c3" ]
    then
        RESULT=9
    fi
}

function changeSymbol() {
    array=$1
    if [ "$2" == "1" ]
    then
        array[$3]="X"
    else
        array[$3]="O"
    fi
}

function errorHandler() {
    if [ $1 -eq 1 ]
    then
        echo "Vous ne pouvez pas jouer sur cette case... Elle est déja prise..."
        echo ""
    fi
}

function Game() {
    clear
    echo "MORPION : "
    echo
    read -p "Entrez le nom du joueur 1 : " player1
    read -p "Entrez le nom du joueur 2 : " player2

    array=(placeholder " " " " " " " " " " " " " " " " " ")
    counter=0
    RESULT=0
    error=0

    while [ 1 -eq 1 ]
    do
    clear
    echo -e "MORPION :"
    echo

    errorHandler $error

    printArray array
    echo ""

    if [ $(($counter % 2)) -eq 0 ]
    then
        askPlay $player1 tmp
        caseToIndex $tmp
        if [ "${array[$RESULT]}" = " " ]
        then
            changeSymbol $array "1" $RESULT
            ((counter++))
        else    
            error=1
        fi
    else
        askPlay $player2 tmp
        caseToIndex $tmp
        if [ "${array[$RESULT]}" = " " ]
        then
            changeSymbol $array "2" $RESULT
            ((counter++))
        else    
            error=1
        fi
    fi

    # Tests Win
    if [ $counter -ge 4 ]
    then
        checkGameStatus array
        echo $GAME
        if [ "$GAME" = "O" ]
        then
            clear
            echo "MORPION :"
            echo ""
            printArray array
            clear
            echo ""
            echo "$player2 a gagné la partie !"
            break
        fi

        if [ "$GAME" = "X" ]
        then
            clear
            echo "MORPION :"
            echo ""
            printArray array
            clear
            echo ""
            echo "$player1 a gagné la partie !"
            break
        fi
    fi

    # Tests loose
    if [ $counter -eq 9 ]
    then
        clear
        echo "MORPION :"
        echo ""
        printArray array
        echo "Match Nul !"
        break
    fi

    done
}

function Menu() {
    while [ 1 -eq 1 ]
    do
        echo "MENU MORPION :"
        echo ""

        echo "1 : Lancer une partie"
        echo "2 : Quitter"

        read MENU
        
        if [ $MENU -eq 1 ]
        then
            Game
        elif [ $MENU -eq 2 ]
        then
            exit 0
        fi
    done
}

Menu