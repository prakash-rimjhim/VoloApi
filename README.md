I have made this project in django rest framework . U have to install either vs code or pycharm to run this code. firstl, i have run the command py -m django startproject ..... to start my project VolopayProject. Then, i have run pip install djangorestframework , for rest framework setup.
Then i have started my app (py manage.py startapp api). Then in installed apps in settings file i have mentioned , my app name and then rest_framework.

i have made model Data with all the details ,  and made aurls and serializer file .
i have write the logic in view file .
 I have used viewset , ModelViewSet , HyperlinkedModelSerializer.
Url -  http://127.0.0.1:8000/api/Data/

I have write the corresponding view for total_items_sold and write the url for that purpose in project url - http://127.0.0.1:8000/api/total_items

I have then write view for nth_most_total_item_view and write corresponding url in project url -http://127.0.0.1:8000/api/nth_most_total_item/.

I have then write view for nth_most_total_item_view and write corresponding url in project url -api/percentage_of_department_wise_sold_items/

I have then write view monthly_sales and write corresponding url in project url - http://127.0.0.1:8000/api/monthly_sales/
