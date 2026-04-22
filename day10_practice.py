"""
Day 10: Practice Exercise - CSV Data Analyzer
"""

import csv
import json

# Step 15: Create sample sales data CSV
def create_sample_data():
    """Create sample sales CSV file"""
    sales_data = [
        ["product", "quantity", "price"],
        ["Laptop", 5, 1200],
        ["Mouse", 50, 25],
        ["Keyboard", 30, 75],
        ["Monitor", 10, 300],
        ["Headphones", 25, 100],
        ["USB Cable", 100, 10],
        ["Webcam", 15, 80]
    ]
    
    try:
        with open("sales_data.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerows(sales_data)
        print("✅ Sample sales data created: sales_data.csv")
        return True
    except Exception as e:
        print(f"❌ Error creating sample data: {e}")
        return False


def analyze_sales(filename):
    """
    Analyze sales data from CSV file.
    Returns dictionary with analysis or None if error.
    """
    try:
        # Check if file exists by trying to open it
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            
            # Initialize counters
            total_revenue = 0
            total_products = 0
            product_revenues = []
            
            print("\n--- Analyzing Sales Data ---")
            print("\nProduct Sales:")
            
            # Process each row
            for row in reader:
                # Validate required fields exist
                if 'product' not in row or 'quantity' not in row or 'price' not in row:
                    print(f"❌ Error: Missing required fields in CSV")
                    return None
                
                # Convert and validate data
                try:
                    quantity = int(row['quantity'])
                    price = int(row['price'])
                except ValueError:
                    print(f"❌ Error: Invalid number in row: {row}")
                    return None
                
                # Calculate revenue
                revenue = quantity * price
                total_revenue += revenue
                total_products += quantity
                
                # Store product info
                product_revenues.append({
                    'product': row['product'],
                    'revenue': revenue
                })
                
                # Display
                print(f"  {row['product']}: {quantity} units × ${price} = ${revenue}")
            
            # Check if we got any data
            if len(product_revenues) == 0:
                print("❌ Error: No data found in CSV file")
                return None
            
            # Calculate statistics
            best_seller = max(product_revenues, key=lambda x: x['revenue'])
            worst_seller = min(product_revenues, key=lambda x: x['revenue'])
            average_sale = total_revenue / len(product_revenues)
            
            # Display results
            print(f"\n💰 Total Revenue: ${total_revenue:,}")
            print(f"📦 Total Products Sold: {total_products}")
            
            print("\n--- Finding Top Performers ---")
            print(f"🏆 Best Seller: {best_seller['product']} (${best_seller['revenue']:,})")
            print(f"📉 Worst Seller: {worst_seller['product']} (${worst_seller['revenue']:,})")
            print(f"📊 Average Sale: ${average_sale:,.2f}")
            
            # Return analysis results
            return {
                "total_revenue": total_revenue,
                "total_products_sold": total_products,
                "average_sale": round(average_sale, 2),
                "number_of_products": len(product_revenues),
                "best_seller": best_seller,
                "worst_seller": worst_seller,
                "all_products": product_revenues
            }
    
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"❌ Error analyzing sales data: {e}")
        return None


def save_report(report, filename):
    """Save report to JSON file"""
    try:
        with open(filename, "w") as f:
            json.dump(report, f, indent=2)
        print(f"\n✅ Report saved to: {filename}")
        return True
    except Exception as e:
        print(f"❌ Error saving report: {e}")
        return False


# Test error cases
if __name__ == "__main__":
    # Normal execution (already done above)
    # Step 1: Create sample data
    if not create_sample_data():
        print("Failed to create sample data. Exiting.")
        exit()
    
    # Step 2: Analyze sales
    analysis = analyze_sales("sales_data.csv")
    
    if analysis:
        # Step 3: Save report
        save_report(analysis, "sales_report.json")
    else:
        print("\n❌ Analysis failed. No report generated.")
    
    # Now test error cases
    print("\n" + "="*50)
    print("TESTING ERROR HANDLING")
    print("="*50)
    
    # Test 1: Missing file
    print("\n--- Test 1: Missing file ---")
    result = analyze_sales("nonexistent.csv")
    if result is None:
        print("✅ Correctly handled missing file")
    
    # Test 2: Corrupted CSV (invalid numbers)
    print("\n--- Test 2: Invalid data in CSV ---")
    corrupted_data = [
        ["product", "quantity", "price"],
        ["Laptop", "five", "1200"],  # "five" is not a number!
    ]
    
    with open("corrupted.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(corrupted_data)
    
    result = analyze_sales("corrupted.csv")
    if result is None:
        print("✅ Correctly handled invalid data")
    
    # Test 3: Empty CSV (only headers)
    print("\n--- Test 3: Empty CSV file ---")
    empty_data = [["product", "quantity", "price"]]
    
    with open("empty.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(empty_data)
    
    result = analyze_sales("empty.csv")
    if result is None:
        print("✅ Correctly handled empty file")
    
    print("\n" + "="*50)
    print("ALL TESTS COMPLETE!")
    print("="*50)