// Database: ml (translated from your phpMyAdmin SQL dump)

// companies table
Table companies {
  id varchar [pk]                 // original: varchar(255) NOT NULL
  company_logo varchar
  company_name varchar
  chart_link varchar
  about_company text
  website varchar
  nse_profile varchar
  bse_profile varchar
  face_value int
  book_value int
  roce_percentage decimal(12,2)
  roe_percentage decimal(12,2)
}

// analysis table
Table analysis {
  id varchar(10) [pk]
  company_id varchar(10) [not null]
  compounded_sales_growth varchar(50)
  compounded_profit_growth varchar(50)
  stock_price_cagr varchar(50)
  roe varchar(50)
}

// prosandcons table
Table prosandcons {
  id int [pk]
  company_id varchar(255)
  pros varchar
  cons varchar
}

// Foreign key relationships
Ref: analysis.company_id > companies.id
Ref: prosandcons.company_id > companies.id
