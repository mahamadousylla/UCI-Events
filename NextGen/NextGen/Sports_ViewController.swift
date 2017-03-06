//
//  Sports_ViewController.swift
//  NextGen
//
//  Created by Mahamadou Sylla on 2/21/17.
//  Copyright © 2017 Mahamadou Sylla. All rights reserved.
//

import UIKit
import Foundation



class Sports_ViewController: UIViewController,
 UITableViewDelegate, UITableViewDataSource {
    
    var buttonClicked = String()
    var tableViewDataSource : [Dictionary<String, String>] = [];
    @IBOutlet weak var tableView: UITableView!
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        
        print(buttonClicked)
        let url = URL(string: "http://127.0.0.1:5000/" + buttonClicked)
        
        
        let task = URLSession.shared.dataTask(with: url!) { data, response, error in
            guard error == nil else {
                print(error!)
                return
            }
            guard let data = data else {
                print("Data is empty")
                return
            }
            
            let json = try! JSONSerialization.jsonObject(with: data, options: []) as! [String:AnyObject]
            
            let myData = (json["data"] as! NSArray) as Array
            for dict in myData {
                self.tableViewDataSource.append(dict as! [String: String])
            }
            
            
            self.tableView.reloadData()
        }
        
        
        
        task.resume()
        
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    
    
        // return the size of the array to tableview
        func tableView(_ tableView: UITableView,numberOfRowsInSection section: Int) -> Int {
            return tableViewDataSource.count
        }
    
        // assign the values in your array variable to cells
        func tableView(_ tableView: UITableView,
                       cellForRowAt indexPath: IndexPath) ->
            UITableViewCell {
    
                // get a reference to our storyboard cell
                print("madeittttt")
                let cell = self.tableView.dequeueReusableCell(withIdentifier: "customCell", for: indexPath) as! Sports_TableViewCell

                
            
                var dict = tableViewDataSource[indexPath.row]
                var a : String!
                a = dict["month"]
                var b : String!
                b = dict["date"]
                var c : String!
                c = dict["location"]
                var d : String!
                d = dict["opponent"]
                var e : String!
                e = dict["score"]
                var f : String!
                f = dict["time"]
                print("what is tableViewDAta", type(of:dict))
                cell.dataLabel!.text = a + " " + b + " " + c + " " + d + " " + e + " " + f
                
//                cell.dataLabel!.text = tableViewDataSource[indexPath.row]
    
    
                return cell;
        }
    

    


    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
