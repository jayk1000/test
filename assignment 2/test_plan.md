Author:Minjae Kim
SID:530009478
Unikey:mkim9138


**Test Cases**
Table 1. Summary of test cases for `buy_cheese` function in `shop.py`. 
| Test ID | Description                    | Inputs                            | Expected Output                | Status |
| ------- | ----------------------         | ------                            | ---------------                | ------ |
| 01      | gold is positive and user 
            inputs correct 
            cheese type and 
            correct cheese quantity 
            - Positive Case                | gold = 200
                                            cheese_amount are Swiss 1, Cheddar 1
                                            , Cheddar 1, and Marble 1 and back | 4 x Successful purchase 
                                                                                (170, (2, 1, 1))                |  Ok      |
| 02      | gold is positive 
            user inputs correct 
            cheese type and correct 
            cheese quantity - Positive Case| gold = 125 
                                            cheese_amount is Swiss 2 and back   |  Successful purchase 
                                                                                    (200, (0, 0, 2))            |  Ok      |
| 03      | user inputs a wrong sequence 
            of cheese_amount. - Negative Case| gold = 100, 
                                                cheese_amount = 1 Swiss, back   |We don't sell 1   (0, (0, 0, 0))|   Ok     |
| 04      | gold is positive and user inputs 
                        nothing- Edge Case| cheese_amount = '', back            | (0, (0, 0, 0))                |   Ok     |
| 05      | user inputs a negative cheese 
            quantity - Nagative case        | gold = 125 
                                            cheese_amount = Cheddar -5, then back| Must purchase 
                                                                                    positive amount of cheese. |  Ok      |
| 06      | gold is positive and user inputs 
        a maximum possible integer- Edge Case| gold = 10*sys.maxsize which is 92233720368547758070
                                            cheese_amount = Cheddar 
                                                            9223372036854775807, back | 
                                                                            (92233720368547758070,(9223372036854775807, 0, 0))      |    Ok    |

Table 2. Summary of test cases for `change_cheese` function in `game.py`.
| Test ID | Description                     | Inputs    | Expected Output       | Status |
| ------- | ----------------------          | ------    | ---------------       | ------ |
|   01    |  given the positive cheese 
          quantity User inputs valid cheese |
          type with a mixture of 
          upper and lowercase  -Positive case|cheese=(["Cheddar", 10], ["Marble", 0], ["Swiss", 0])
                                            cHeDdAR, yes|  (True, Cheddar)     |    Ok    |
|   02    |  given the positive cheese 
          quantity
          User inputs valid cheese 
          but says no when asked again then exits
                -Positive case              |cheese=(["Cheddar", 0], ["Marble", 0], ["Swiss", 1])
                                            Swiss, no, back|    (False, None)     |   Ok     |
|   03    |user inputs a number rather 
                than a cheese type 
                - Negative case
                                            | 23, back       | No such cheese.  (False, None)|  Ok      |
|   04    |
          User inputs a special character ESC
                - Negative case             |cheese=(["Cheddar", 0], ["Marble", 0], ["Swiss", 1]) 
                                              ESC, back     |   No such cheese.  (False, None)  | Ok       |
|   05    | given the empty string as the only cheese type and its positive
          in cheese list
          user inputs an empty string
            - Edge case                    | cheese=(['', 0])
                                           | '', yes, back | (True, '')                         |  Fail      |
|   06    |given the trap as an empty string
        as well as cheese quantity 
        is an empty string
        User inputs valid cheese type | cheese=(["Cheddar", ''], ["Marble", 0], ["Swiss", 1])
                                                                |  Type error                   | Fail       |