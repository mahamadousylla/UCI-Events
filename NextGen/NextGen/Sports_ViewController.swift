//
//  Sports_ViewController.swift
//  NextGen
//
//  Created by Mahamadou Sylla on 2/21/17.
//  Copyright © 2017 Mahamadou Sylla. All rights reserved.
//

import UIKit
//import PlaygroundSupport
import Foundation

class Sports_ViewController: UIViewController {

    @IBOutlet weak var tableView: UITableView!
    override func viewDidLoad() {
        super.viewDidLoad()
        
        
//        let url = URL(string: "http://127.0.0.1:5000/m-baskbl")
//        
//        let task = URLSession.shared.dataTask(with: url!) { data, response, error in
//            guard error == nil else {
//                print(error!)
//                return
//            }
//            guard let data = data else {
//                print("Data is empty")
//                return
//            }
//            
//            let json = try! JSONSerialization.jsonObject(with: data, options: [])
//            print(json)
//        }
//        
//        task.resume()
        
        // Do any additional setup after loading the view.
    }


    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

//    var tableViewDataSource = ["One", "Two", "Three",
//                               "Four", "Five", "Six"];
//
//    
//    // return the size of the array to tableview
//    func tableView(_ tableView: UITableView,
//                   numberOfRowsInSection section: Int) -> Int {
//        return tableViewDataSource.count
//    }
//    
//    // assign the values in your array variable to cells
//    func tableView(_ tableView: UITableView,
//                   cellForRowAt indexPath: IndexPath) ->
//        UITableViewCell {
//            
//            // get a reference to our storyboard cell
//            
//            let cell = self.tableView.dequeueReusableCell(withIdentifier: "customCell", for: indexPath) as! Sports_TableViewCell
//            
//            //let cell:UITableViewCell=UITableViewCell(withIdentifier: "cell", for: indexPath) as! TableViewCell
//            
//            // "label!" is the pizzaLabel
//            cell.dataLabel!.text = tableViewDataSource[indexPath.row]
//            
//            
//            return cell;
//    }
//    
//    // Register when user taps a cell via alert message
//    func tableView(_ tableView: UITableView,didSelectRowAt indexPath: IndexPath) {
//        let alert = UIAlertController(title: "Selected Cell:", message: tableViewDataSource[indexPath.row], preferredStyle: UIAlertControllerStyle.alert)
//        alert.addAction(UIAlertAction(title: "Okay", style:
//            UIAlertActionStyle.default, handler: nil))
//        self.present(alert, animated: true, completion:nil)
//    }
    


    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
