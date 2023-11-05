few_shots = [
    {'Question' : "How many ev_cars do we have left for Tata in premium_customized model and white color?",
     'SQLQuery' : "SELECT stock FROM ev_cars WHERE brand = 'Tata' AND color = 'White' AND model = 'premium_customized'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "100"},
    {'Question' : "How many tesla do we have left for tesla in premium model and white color?",
     'SQLQuery' : "SELECT stock FROM ev_cars WHERE brand = 'Tesla' AND model = 'premium' AND color = 'white'",
     'SQLResult': "Result of the SQL query",
     'Answer' : "155"},
    {'Question': "How much is the total price of the inventory for all base-model evcars?",
     'SQLQuery':"SELECT SUM(price) FROM ev_cars WHERE model = 'base'",
     'SQLResult': "Result of the SQL query",
     'Answer': "266856509"},
    {'Question': "If we have to sell all the Tesla ev_cars today with discounts applied. How much revenue  our store will generate (post discounts)?" ,
     'SQLQuery' : """SELECT SUM(a.total_amount * ((100 - COALESCE(discounts.percentage_discount, 0)) / 100)) AS total_revenue
FROM (
    SELECT SUM(price * stock) AS total_amount, ev_car_id
    FROM ev_cars
    WHERE brand = 'Tesla'
    GROUP BY ev_car_id
) a
LEFT JOIN discounts ON a.ev_car_id = discounts.ev_car_id;
 """,
     'SQLResult': "Result of the SQL query",
     'Answer': "16725.4"} ,
     {'Question' : "If we have to sell all the Mahindra Car today. How much revenue our store will generate without discount?" ,
      'SQLQuery': """SELECT SUM(CAST(price AS BIGINT) * CAST(stock AS BIGINT)) AS total_price
    FROM Cars
    WHERE brand = 'Mahindra';""",
      'SQLResult': "Result of the SQL query",
      'Answer' : "30126787806"},
    {'Question': "How many white color and green color Tesla's car I have?",
     'SQLQuery' : "SELECT COUNT(*) FROM ev_cars WHERE brand = 'Tesla' AND (color = 'Green' OR color = 'White')",
     'SQLResult': "Result of the SQL query",
     'Answer' : "68"
     },
    {'Question': "how much sales amount will be generated if we sell all premium electric cars today in Tata brand after discounts?",
     'SQLQuery' : """SELECT SUM(a.total_amount * ((100 - COALESCE(discounts.percentage_discount, 0)) / 100)) AS total_revenue
FROM (
    SELECT SUM(price * stock_quantity) AS total_amount, ev_car_id
    FROM ev_cars
    WHERE brand = 'Tata' AND model = 'premium'
    GROUP BY ev_car_id
) a
LEFT JOIN discounts ON a.ev_car_id = discounts.ev_car_id;
 """,
     'SQLResult': "Result of the SQL query",
     'Answer' : "290"
    }
]
