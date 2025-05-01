alert("DONE")
function action(type) {
    switch(type) {
      case 'invoice':
        document.getElementById('sales').innerText = '₹5000';
        document.getElementById('purchase').innerText = '₹3000';
        alert('Creating a new invoice...');
        break;
  
      case 'add_customer':
        alert('Redirecting to add new customer...');
        break;
  
      case 'add_medicine':
        alert('Redirecting to add new medicine...');
        break;
  
      case 'add_supplier':
        alert('Redirecting to add new supplier...');
        break;
  
      case 'add_purchase':
        alert('Redirecting to add new purchase...');
        break;
  
      case 'sales_report':
        alert('Generating sales report...');
        break;
  
      case 'sales_purchase':
        alert('Generating combined sales & purchase report...');
        break;
  
      default:
        alert('Unknown action: ' + type);
    }
  }