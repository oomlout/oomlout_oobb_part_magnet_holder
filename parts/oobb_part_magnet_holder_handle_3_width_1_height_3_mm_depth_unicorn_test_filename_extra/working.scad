//import unicorn.stl
//translate -10,-10-,10

difference(){
    union(){
        rotate(a=[0,0,0]){
            translate(v=[0,0,0]){
            //rotate 90,90,90
            
                scale(v = v){ 
                import(file = "unicorn.stl", convexity = 10);
                }
            }
        }
    }
    union(){
        si = 1000;
        #translate(v=[0,0,-si/2]){
            cube([si,si,si], center = true);
        }
    }
}