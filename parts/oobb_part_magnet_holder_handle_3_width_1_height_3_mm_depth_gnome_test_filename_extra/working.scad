//import unicorn.stl
//translate -10,-10-,10

difference(){
    union(){
        rotate(a=[0,0,0]){
            translate(v=[0,0,0]){
            //rotate 90,90,90
                v =[1,1,1];
                scale(v = v){ 
                import(file = "source.stl", convexity = 10);
                }
            }
        }
    }
    union(){
        si = 1000;
        translate(v=[0,0,-si/2]){
            cube([si,si,si], center = true);
        }
    }
}