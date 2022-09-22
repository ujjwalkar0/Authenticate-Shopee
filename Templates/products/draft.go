  {% comment %}


  {% if user_type == "Delivery Boy" %}

  <input type="text" placeholder="Enter Area Pin No" class="form-control"/>

  <div class="w3-bar w3-light-grey">
    {% if pin_no_by_id %}
    <a href="/ip/update/{{pin_no_by_id}}" class="w3-bar-item w3-button">Change PIN No.</a>
    {% else %}
    <a href="/ip/create" class="w3-bar-item w3-button">Register Your PIN No.</a>
   {% endif %}
    </div>
  </div>
  <div id="product"
  style="margin: 50px 30px"></nav>
    <h3> Delivery Requests </h3>
    <div class="row row-cols-1 row-cols-sm-1 row-cols-lg-1 row-cols-xl-1 ">
    
    {% for post in orders %}
      <div class="col mb-12" style="margin: 10px;">
    <div class="card card-cascade wider">
    
       <!-- Start your project here-->
     <div id="carousel-example-multi" class="carousel slide carousel-multi-item v-2" data-ride="carousel">
    
      <div class="carousel-inner" role="listbox">
        <div class="carousel-item active">
          <div class="card-body ">
    
              <a href="{% url 'mobiles-details' post.pk %}">

                <!-- <h4 class="card-title text-left" ><strong>{{post.address}}</strong></h4> -->
              </a>
              <!-- <div>
              <h5 class="green-text" style="float: left;"> <strong>Price :- {{post.address}}</strong></h5><br>
            </div> -->
            <h3>Address To Deliver :- </h3>
              <p class="card-text text-left">{{post.address|slice:":100"}}
              <br />

              <h3>Quantity :- </h3>
              <p class="card-text text-left">{{post.quantity}}
              <br />
                            
              <div class="card-footer text-muted text-center mt-4">
               <a class="red-text" href="{{ post.product_id }}">View The Product</a>
               <a class="btn btn-green w3-right" href="orders/{{post.id}}"> Reply</a>

              </div>
          
            </div> 
            </div>
      </div>
    </div>
    </div>
    </div>
    {% endfor %}
    </div>
    
  


  <!------------------------------------------------------------>
    {% elif user_type == "Customer"  %}
  
  <div class="w3-bar w3-light-grey">
    {% if user.is_authenticated %}
    {% if pin_no_by_id %}
    <a href="/ip/update/{{pin_no_by_id}}" class="w3-bar-item w3-button">Change PIN No.</a>
    <a href="/orders" class="w3-bar-item w3-button">My Orders</a>

    {% else %}
    <a href="/ip/create" class="w3-bar-item w3-button">Register Your PIN No.</a>
   {% endif %}
   {% else %}
   <h2>Please Login To See products of nearby shops</h2>
   {% endif %}





    </div>

  </div>
  <div id="product"
  style="margin: 50px 30px"></nav>

  <!-------------------------- Mobiles ------------------------------------>
  <h3> Mobiles & Accessories </h3>
  <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3 row-cols-xl-4 ">
  
  {% for product in object_list %}
    <div class="col mb-3">
  <div class="card card-cascade wider">
  
     <!-- Start your project here-->
   <div id="carousel-example-multi" class="carousel slide carousel-multi-item v-2" data-ride="carousel">
  
    <div class="carousel-inner" role="listbox">
      <div class="carousel-item active">
        {% if product.image %}
        <img class="card-img-top center" src="/media/{{product.image}}" 
        style="height: 200px;
        width:100px;
        display: block;
        margin-left: auto;
        margin-right: auto;"

        alt="{{product.image}} image">
        {% else %}
        <img class="card-img-top center" src="{{product.Product_img_link}}" 
        style="height: 200px;
        width:100px;
        display: block;
        margin-left: auto;
        margin-right: auto;"

        alt="{{product.Product_name}} image">
        {% endif %}

        <div class="card-body ">
  
            <a href="/details/{{product.id}}">
              <h4 class="card-title text-left" ><strong>{{product.Product_name}}</strong></h4>
            </a>
            <div>
            <h5 class="green-text" style="float: left;"> <strong>Price :- {{product.Product_price}}</strong></h5><br>
          </div>
            <br />
            <p class="card-text text-left">{{product.feature|slice:":100"}}........
            <br />
              <a style="float: right;" href="/details/{{product.id}}" style="color: blue;"> Read More >> </a></p>
            <br>
            
            
            <div class="card-footer text-muted text-center mt-4">
              {{ product.product_date }}
            </div>
        
          </div> 
          </div>
    </div>
  </div>
  </div>
  </div>
  {% endfor %}
  </div>
  
  <!--------------------------------------------------------------/>
  
  <!*--------------------  Cars  -------------------------------->
  <br>
  <h3> Cars </h3>
  <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4 ">
  
    {% for post in cars %}
      <div class="col mb-3">
    <div class="card card-cascade wider">
    
       <!-- Start your project here-->
     <div id="carousel-example-multi" class="carousel slide carousel-multi-item v-2" data-ride="carousel">
    
      <div class="carousel-inner" role="listbox">
        <div class="carousel-item active">

          <img class="card-img-top" src="/media/{{post.image}}"
          alt="Card image cap">
          <div class="card-body ">
    
              <a href="{% url 'car-details' post.pk %}">
                <h4 class="card-title text-left" ><strong>{{post.name}}</strong></h4>
              </a>
              <div>
              <h5 class="blue-text"> <strong>Price :- {{post.selling_price}}</strong></h5>
              <h5 class="blue-text"> <strong>Year :- {{post.year}}</strong></h5>
              <h5 class="blue-text"> <strong>Km Driven :- {{post.km_driven}}</strong></h5>
              <h5 class="blue-text"> <strong>Fuel :- {{post.fuel}}</strong></h5>
              <h5 class="blue-text"> <strong>Seller Type :- {{post.seller_type}}</strong></h5>
              <h5 class="blue-text"> <strong>Transmission :- {{post.transmission}}</strong></h5>
              <h5 class="blue-text"> <strong>Owner :- {{post.owner}}</strong></h5>
            </div>
              <br />

                {% if user.is_superuser %}
                <br>
              <a href="{% url 'car_delete' post.pk %}"><button class="btn w3-red" style="float: left;">Delete</button></a>
              <a href="{% url 'car_update' post.pk %}"><button class="btn w3-green" style="float: right;">Edit</button></a>
              <br><br>
      
              {% endif %}
              
              <div class="card-footer text-muted text-center mt-4">
                {{ post.post_date }}
              </div>
          
            </div> 
            </div>
      </div>
    </div>
    </div>
    </div>
    {% endfor %}
    </div>
    
      <!--------------------  Others  -------------------------------->
<h3>Other Products</h3>
      <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4 ">

        {% for post in products %}
          <div class="col mb-4">
        <div class="card card-cascade wider">
        
           <!-- Start your project here-->
         <div id="carousel-example-multi" class="carousel slide carousel-multi-item v-2" data-ride="carousel">
        
          <div class="carousel-inner" role="listbox">
            <div class="carousel-item active">
  
              <img class="card-img-top" src="/media/{{post.image}}"
              alt="Card image cap">
  
              <div class="card-body ">
        
                  <a href="{% url 'article-details' post.pk %}">
                    <h4 class="card-title text-left" ><strong>{{post.title}}</strong></h4>
                  </a>
                  <div>
                  <h5 class="green-text" style="float: left;"> <strong>Price :- {{post.price}}</strong></h5>
                  <h5 class="green-text" style="float: right;"> <strong>Stock :- {{post.stock}}</strong></h5></div>
                  <br />
                  <a href="{% url 'catagoryview' post.catagory %}">
                    <h5 class="blue-text pb-2 text-right"><strong>{{post.catagory}}</strong></h5>
                  </a>
                  <p class="card-text text-left">{{post.body|slice:":100"}}........
                  <br />
                    <a style="float: right;" href="{% url 'article-details' post.pk %}" style="color: blue;"> Read More >> </a></p>
      
    {% if user.is_superuser %}   
                    <br>
                  <a href="{% url 'delete' post.pk %}"><button class="btn w3-red" style="float: left;">Delete</button></a>
                  <a href="{% url 'update' post.pk %}"><button class="btn w3-green" style="float: right;">Edit</button></a>
                  <br><br>
    {% endif %}
       
                  
                  <div class="card-footer text-muted text-center mt-4">
                    {{ post.post_date }}
                  </div>
              
                </div> 
                </div>
          </div>
        </div>
        </div>
        </div>
        {% endfor %}
        </div>
  <!--------------------------------------------------------------->
  
  <!-- {% if page_obj.has_previous %}
  <a href="?page={{page_obj.previous_page_number}}"><button class="w3-btn w3-yellow" style="float: left;">Previous Page</button></a>
  {% endif %}
  {% if page_obj.has_next %}
  <a href="?page={{page_obj.next_page_number}}"><button class="w3-btn w3-cyan" style="float: right;">Next Page</button></a>
  {% endif %} -->
  
{% endif %} {% endcomment %}
