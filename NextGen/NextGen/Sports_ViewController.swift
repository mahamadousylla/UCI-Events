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

    @IBOutlet weak var tableView: UITableView!
    var tableViewDataSource = [] as Array;
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        
        let url = URL(string: "http://127.0.0.1:5000/m-baskbl")
        
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
//                var s = dict["date"] + " " + dict["location"]  + " " + dict["month"]  + " "
//                + dict["opponent"] + " " + dict["score"] + " " + dict["time"]
                self.tableViewDataSource.append(dict)
            }
            
//            print(self.tableViewDataSource)
        }
        
//        task.resume()
        
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
//    func returnExampleArray() -> [Array<Any>] {
    
    
//        var tableViewDataSource = ["One", "Two", "Three",
//                                   "Four", "Five", "Six"];
    
    
        // return the size of the array to tableview
        func tableView(_ tableView: UITableView,numberOfRowsInSection section: Int) -> Int {
            print("Here tableView")
//            print(table_ViewDataSource.count)
            print(self.tableViewDataSource.count)
            return self.tableViewDataSource.count
        }
    
        // assign the values in your array variable to cells
        func tableView(_ tableView: UITableView,
                       cellForRowAt indexPath: IndexPath) ->
            UITableViewCell {
    
                // get a reference to our storyboard cell
                print("madeittttt")
                let cell = self.tableView.dequeueReusableCell(withIdentifier: "customCell", for: indexPath) as! Sports_TableViewCell
    
                //let cell:UITableViewCell=UITableViewCell(withIdentifier: "cell", for: indexPath) as! TableViewCell
    
                //print(tableViewDataSource)
                
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