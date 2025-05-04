
## **System Documentation: Pharmacy Management System (PMS)**

This document outlines the development and features of the **Pharmacy Management System (PMS)**, a web-based application designed to facilitate pharmacy operations. The system provides users and administrators with the tools to manage inventory, orders, and user interactions in an intuitive and efficient manner.

---

### **Overview of the Pharmacy Management System**

![Home Page](https://raw.githubusercontent.com/ToYoNiX/pharmacy-management-system/main/Documentation/assets/Pasted%20image%2020250503122229.png)

The Pharmacy Management System (PMS) is designed to streamline and optimize various pharmacy operations. The system is built using the **Django** framework for backend development, with **HTML**, **CSS**, and **JavaScript** powering the frontend. It uses **SQLite3** as the database engine to provide a lightweight yet reliable data management solution.

The development process followed the **Agile** methodology, ensuring flexibility and rapid iterations. Development began on **March 8** and was completed by **May 3**, marking a focused and productive development cycle. The timeline and progress of tasks are documented at the end of this report.

---

### **Key Components of PMS**

The PMS consists of three core components:

1. **Admin Application**:
    
    - Manages inventory (adding/removing medicines), and handles administrative tasks.
        
2. **Marketplace Application**:
    
    - Allows users to browse and order medicines directly through the system.
        
3. **Accounts Application** (Internal):
    
    - Manages user authentication, permissions, and roles within the system. This application controls the roles of users (regular clients, pharmacy admins, and super admins) and enforces access control throughout the platform.
        

---

### **User Roles and Permissions**

The system distinguishes between three primary user roles, each with specific permissions:

1. **Regular Client**:
    
    - Can browse products, add them to their cart, and place orders.
        
2. **Pharmacy Admin**:
    
    - Can add and remove products, as well as manage the inventory.
        
3. **Super Admin**:
    
    - Has the highest level of access and control over the system, including enabling/disabling applications using Django's shell and performing system-wide administrative tasks.
        

The **Accounts** application is responsible for managing user roles and permissions, utilizing Python decorators for role-based access control.

---

### **Common Features for All Users**

The following features are accessible to all users of the system:

1. **Search for Products**:
    
    - Users can search for specific medicines or products by name or category.
    ![Search](https://raw.githubusercontent.com/ToYoNiX/pharmacy-management-system/main/Documentation/assets/Pasted%20image%2020250503122319.png)

2. **View Categories**:
    
    - Users can view available categories of medicines.
    ![Categories](https://raw.githubusercontent.com/ToYoNiX/pharmacy-management-system/main/Documentation/assets/Pasted%20image%2020250503122357.png)
3. **Add to Cart**:
    
    - Users can add selected items to their shopping cart.
    ![Add to Cart](https://raw.githubusercontent.com/ToYoNiX/pharmacy-management-system/main/Documentation/assets/Pasted%20image%2020250503122414.png)

4. **Update Cart Items**:
    
    - Users can modify the quantity of items in their cart or remove them.
    ![Update Cart](https://raw.githubusercontent.com/ToYoNiX/pharmacy-management-system/main/Documentation/assets/Pasted%20image%2020250503122437.png)

5. **Login and Register**:
    
    - Users can register for an account or log in to access personalized features such as viewing their cart and placing orders.
    ![Login and Register](https://raw.githubusercontent.com/ToYoNiX/pharmacy-management-system/main/Documentation/assets/Pasted%20image%2020250503122448.png)

---

### **Admin-Specific Features**

The following features are exclusive to administrators:

![Admin Dashboard](https://raw.githubusercontent.com/ToYoNiX/pharmacy-management-system/main/Documentation/assets/Pasted%20image%2020250503122701.png)

1. **Add Category**:
    
    - Admins can create new categories to organize products.
    ![Add Category](https://raw.githubusercontent.com/ToYoNiX/pharmacy-management-system/main/Documentation/assets/Pasted%20image%2020250503122724.png)

2. **Add Product**:
    
    - Admins can add new products to the inventory, including product details such as price, description, and stock level.
    ![Add Product](https://raw.githubusercontent.com/ToYoNiX/pharmacy-management-system/main/Documentation/assets/Pasted%20image%2020250503122716.png)

---

### **Database Structure**

The database is managed through Django’s ORM (Object-Relational Mapping), and the models are defined within each application. The database schema includes tables for products, categories, users, carts, and orders. Each application is responsible for managing its own set of models, though the **Accounts** application plays a central role in managing user authentication and permissions.

---

### **Model and Relationships Documentation**

---

#### **1. Category (Marketplace)**

- **Fields**:
    
    - `name`: A unique string representing the category name (max length 255 characters).
        
    - `description`: A text field describing the category (optional).
        
- **Behavior**:
    
    - The category name is automatically saved in lowercase to maintain consistency.
        
- **Table**: `marketplace_category`
    

---

#### **2. Product (Marketplace)**

- **Fields**:
    
    - `category`: A foreign key relationship to the `Category` model, linking a product to a category.
        
    - `name`: A string representing the product name (max length 255 characters).
        
    - `description`: A text field for additional product information (optional).
        
    - `price`: A decimal representing the price of the product.
        
    - `stock`: A positive integer representing the quantity of the product available.
        
    - `image_url`: A URL field for the product's image (optional).
        
    - `expiry_date`: A date field indicating the expiration date of the product (optional).
        
- **Table**: `marketplace_product`
    
- **Relationships**:
    
    - A product belongs to a single category, and each category can have multiple products (One-to-many).
        

---

#### **3. Cart (Marketplace)**

- **Fields**:
    
    - `user`: A foreign key relationship to the `User` model (from the **Accounts** application) representing the user who owns the cart.
        
    - `created_at`: A timestamp representing when the cart was created (auto-generated).
        
- **Table**: `marketplace_cart`
    
- **Relationships**:
    
    - Each cart is associated with a single user (One-to-many relationship between `User` and `Cart`).
        

---

#### **4. CartItem (Marketplace)**

- **Fields**:
    
    - `cart`: A foreign key relationship to the `Cart` model, linking the cart item to a specific cart.
        
    - `product`: A foreign key relationship to the `Product` model, representing the product added to the cart.
        
    - `quantity`: An integer representing the number of units of the product in the cart.
        
- **Table**: `marketplace_cartitem`
    
- **Relationships**:
    
    - Each cart item is linked to a single `Cart` and a single `Product`. A cart can have multiple cart items (One-to-many between `Cart` and `CartItem`).
        

---

#### **5. Order (Marketplace)**

- **Fields**:
    
    - `user`: A foreign key relationship to the `User` model (from the **Accounts** application) representing the user who placed the order.
        
    - `cart`: A one-to-many relationship with the `Cart` model.
        
    - `total_price`: A decimal representing the total price of the order.
        
    - `status`: A string indicating the current order status (choices: `pending`, `confirmed`, `shipped`, `delivered`).
        
    - `created_at`: A timestamp representing when the order was placed (auto-generated).
        
- **Table**: `marketplace_order`
    
- **Relationships**:
    
    - Each order is associated with a single user and a specific cart (One-to-many relationship between `Cart` and `Order`).
        

---

#### **6. User (Accounts)**

- **Fields**:
    
    - `email`: A unique email address representing the user.
        
    - `role`: A string indicating the user’s role (`customer` or `admin`).
        
    - `is_active`: A boolean indicating if the user account is active.
        
    - `is_staff`: A boolean indicating if the user has admin access.
        
- **Table**: `accounts_user`
    
- **Relationships**:
    
    - A user can have multiple carts and orders (One-to-many relationship with `Cart` and `Order`).
        

---

### **Relationships Overview**

- **User to Cart**: One-to-many relationship (A user can have multiple carts).
    
- **User to Order**: One-to-many relationship (A user can place multiple orders).
    
- **Category to Product**: One-to-many relationship (A category can have multiple products).
    
- **Cart to CartItem**: One-to-many relationship (A cart can contain multiple items).
    
- **Product to CartItem**: One-to-many relationship (A product can appear in multiple cart items).
    
- **Cart to Order**: One-to-many relationship (A cart can belong to multible orders).

---

### **Database Table Summary**

| Table Name             | Model Name | Key Fields                                          | Relationships                                       |
| ---------------------- | ---------- | --------------------------------------------------- | --------------------------------------------------- |
| `marketplace_category` | `Category` | `name`, `description`                               | One-to-many with `Product`                          |
| `marketplace_product`  | `Product`  | `category`, `name`, `price`, `stock`, `expiry_date` | Many-to-one with `Category`                         |
| `marketplace_cart`     | `Cart`     | `user`, `created_at`                                | Many-to-one with `User`                             |
| `marketplace_cartitem` | `CartItem` | `cart`, `product`, `quantity`                       | Many-to-one with `Cart`, Many-to-one with `Product` |
| `marketplace_order`    | `Order`    | `user`, `cart`, `total_price`, `status`             | One-to-many with `Cart`, Many-to-many with `User`   |
| `accounts_user`        | `User`     | `email`, `role`, `is_active`, `is_staff`            | One-to-many with `Cart`, One-to-many with `Order`   |
