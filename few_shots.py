few_shots = [
    {'Question' : "How many ev_cars do we have left for Tata in premium_customized model and white color?",
     'SQLQuery' : "SELECT sum(stock_quantity) FROM ev_cars WHERE brand = 'Tata' AND color = 'White' AND model = 'premium_customized'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "91"},
    {'Question': "How much is the total price of the inventory for all S-model evcars?",
     'SQLQuery':"SELECT SUM(price*stock_quantity) FROM ev_cars WHERE model = 'premium'",
     'SQLResult': "Result of the SQL query",
     'Answer': "222920"},
    {'Question': "If we have to sell all the Tesla ev_cars today with discounts applied. How much revenue  our store will generate (post discounts)?" ,
     'SQLQuery' : """SELECT sum(a.total_amount * ((100-COALESCE(discounts.percentage_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, ev_car_id from ev_cars where brand = 'Tesla'
group by ev_car_id) a left join discounts on a.ev_car_id = discounts.ev_car_id
 """,
     'SQLResult': "Result of the SQL query",
     'Answer': "16725.4"} ,
     {'Question' : "If we have to sell all the Tesla Car today. How much revenue our store will generate without discount?" ,
      'SQLQuery': "SELECT SUM(price * stock_quantity) FROM Cars WHERE brand = 'Tesla",
      'SQLResult': "Result of the SQL query",
      'Answer' : "17462"},
    {'Question': "How many white color Tesla's shirt I have?",
     'SQLQuery' : "SELECT sum(stock_quantity) FROM ev_cars WHERE brand = 'Tesla' AND color = 'White'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "290"
     },
    {'Question': "how much sales amount will be generated if we sell all premium electric cars today in Tata brand after discounts?",
     'SQLQuery' : """SELECT sum(a.total_amount * ((100-COALESCE(discounts.percentage_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, ev_car_id from ev_cars where brand = 'Tata' and model="premium"
group by ev_car_id) a left join discounts on a.ev_car_id = discounts.ev_car_id
 """,
     'SQLResult': "Result of the SQL query",
     'Answer' : "290"
    }
]
