import copy
import opsc
import oobb
import oobb_base
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    typ = kwargs.get("typ", "")

    if typ == "":
        #setup    
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    #oomp_mode = "project"
    oomp_mode = "oobb"

    test = False
    #test = True

    if typ == "all":        
        #no overwrite
        filter = ""; save_type = "all"; navigation = True; overwrite = False; modes = ["3dpr"]; oomp_run = True; test = False
        #default
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True; test = False
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
        #default
        #filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
    elif typ == "manual":
    #filter
        filter = ""
        #filter = "test"

    #save_type
        save_type = "none"
        #save_type = "all"
        
    #navigation        
        #navigation = False
        navigation = True    

    #overwrite
        overwrite = True
                
    #modes
        #modes = ["3dpr", "laser", "true"]
        modes = ["3dpr"]
        #modes = ["laser"]    

    #oomp_run
        oomp_run = True
        #oomp_run = False    

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    kwargs["oomp_run"] = oomp_run
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]
        #max 60 characters
        length_max = 40
        if len(project_name) > length_max:
            project_name = project_name[:length_max]
            #if ends with a _ remove it 
            if project_name[-1] == "_":
                project_name = project_name[:-1]
                
        #defaults
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        #oomp_bits
        if oomp_mode == "project":
            kwargs["oomp_classification"] = "project"
            kwargs["oomp_type"] = "github"
            kwargs["oomp_size"] = "oomlout"
            kwargs["oomp_color"] = project_name
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""
        elif oomp_mode == "oobb":
            kwargs["oomp_classification"] = "oobb"
            kwargs["oomp_type"] = "part"
            kwargs["oomp_size"] = ""
            kwargs["oomp_color"] = ""
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        part_default = {} 
       
        part_default["project_name"] = project_name
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        ps = []

        p = {}        
        p["magnet"] = "hardware_magnet_cylinder_6_mm_diameter_6_mm_depth"
        p["width"] = 3
        p["height"] = 1
        p["magnet_shape"] = "cylinder"
        p["magnet_diameter"] = 6
        p["magnet_depth"] = 6
        p["magnet_multiple"] = 3
        p["magnet_offset"] = 7.5
        ps.append(p)

        
        p = {}        
        p["magnet"] = "hardware_magnet_cylinder_12_mm_diameter_3_mm_depth"
        p["width"] = 4
        p["height"] = 1
        p["magnet_shape"] = "cylinder"
        p["magnet_diameter"] = 12
        p["magnet_depth"] = 3
        p["magnet_multiple"] = 2
        p["magnet_offset"] = 15
        ps.append(p)

        p = {}        
        p["magnet"] = "hardware_magnet_cylinder_10_mm_diameter_3_mm_depth"
        p["width"] = 3
        p["height"] = 1
        p["magnet_shape"] = "cylinder"
        p["magnet_diameter"] = 10
        p["magnet_depth"] = 3
        p["magnet_multiple"] = 2
        p["magnet_offset"] = 12
        ps.append(p)

        #rectangule
        p = {}
        p["magnet"] = "hardware_magnet_rectangle_29_mm_length_9_5_mm_width_3_mm_depth"
        p["width"] = 4
        p["height"] = 1
        p["magnet_shape"] = "rectangle"
        p["magnet_length"] = 29
        p["magnet_width"] = 9.5
        p["magnet_depth"] = 3
        p["magnet_multiple_x"] = 1
        p["magnet_offset_x"] = 0
        p["magnet_multiple_y"] = 1
        p["magnet_offset_y"] = 0
        ps.append(p)

        #20x3x2 y_multiple 2 y offset6
        p = {}
        p["magnet"] = "hardware_magnet_rectangle_20_mm_length_3_mm_width_2_mm_depth"
        p["width"] = 3
        p["height"] = 1
        p["magnet_shape"] = "rectangle"
        p["magnet_length"] = 20
        p["magnet_width"] = 3
        p["magnet_depth"] = 2
        p["magnet_multiple_x"] = 1
        p["magnet_offset_x"] = 0
        p["magnet_multiple_y"] = 2
        p["magnet_offset_y"] = 6
        ps.append(p)

        #20x3x2 y_multiple 2 y offset6
        p = {}
        p["magnet"] = "hardware_magnet_rectangle_20_mm_length_3_mm_width_3_mm_depth"
        p["width"] = 3
        p["height"] = 1
        p["magnet_shape"] = "rectangle"
        p["magnet_length"] = 20
        p["magnet_width"] = 3
        p["magnet_depth"] = 3
        p["magnet_multiple_x"] = 1
        p["magnet_offset_x"] = 0
        p["magnet_multiple_y"] = 2
        p["magnet_offset_y"] = 6
        ps.append(p)

        #20x6x3 y_multiple 1 y offset 0
        p = {}
        p["magnet"] = "hardware_magnet_rectangle_20_mm_length_6_mm_width_3_mm_depth"
        p["width"] = 3
        p["height"] = 1
        p["magnet_shape"] = "rectangle"
        p["magnet_length"] = 20
        p["magnet_width"] = 6
        p["magnet_depth"] = 3
        p["magnet_multiple"] = 1
        p["magnet_offset"] = 0
        ps.append(p)

        #20x10x2 y_multiple 1 y offset 0
        p = {}
        p["magnet"] = "hardware_magnet_rectangle_20_mm_length_10_mm_width_2_mm_depth"
        p["width"] = 3
        p["height"] = 1
        p["magnet_shape"] = "rectangle"
        p["magnet_length"] = 20
        p["magnet_width"] = 10
        p["magnet_depth"] = 2
        p["magnet_multiple"] = 1
        p["magnet_offset"] = 0
        ps.append(p)

        #20x4.5x3 y_multiple 1 y offset 0
        p = {}
        p["magnet"] = "hardware_magnet_rectangle_20_mm_length_4_5_mm_width_3_mm_depth"
        p["width"] = 3
        p["height"] = 1
        p["magnet_shape"] = "rectangle"
        p["magnet_length"] = 20
        p["magnet_width"] = 4.5
        p["magnet_depth"] = 3
        p["magnet_multiple"] = 1
        p["magnet_offset"] = 0
        ps.append(p)





        for p in ps:
            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            p3.update(p)
            p3["thickness"] = p3["magnet_depth"] + .5            

            if p3.get("magnet_multiple", None) is not None:                
                ex = f"{p3["magnet"]}_magnet"
            if p3.get("magnet_multiple_x", None) is not None:
                ex = f"{p3["magnet"]}_magnet_{p3["magnet_multiple_x"]}_multiple_x_{p3["magnet_multiple_y"]}_multiple_y"
            p3["extra"] = ex
            part["kwargs"] = p3
            nam = f"magnet_holder"
            part["name"] = nam
            if oomp_mode == "oobb":
                p3["oomp_size"] = nam
            if not test:
                pass
                parts.append(part)

        ps = []

        
        
        messages = ["","A","H","HELEN", "AARON", "CLAIRE"]

        for m in messages:

            p = {}
            p["shape_full"] = "cylinder_30_mm_diameter"
            p["shape"] ="oobb_cylinder"
            p["shape_radius"] = 30/2        
            p["shape_depth"] = 6
            p["message"] = m
            p["width"] = 3
            p["height"] = 1
            p["thickness"] = 6
            ps.append(p)

            p = copy.deepcopy(p)
            p["width"] = 4
            ps.append(p)

        

        for p in ps:
            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            p3.update(p)
            shape_full = p3["shape_full"]           
            p3["extra"] = f"{shape_full}_shape"
            message = p3.get("message", "")
            if message != "":
                p3["extra"] += f"_{message}_message"            
            part["kwargs"] = p3
            nam = f"magnet_holder_handle"
            part["name"] = nam
            if oomp_mode == "oobb":
                p3["oomp_size"] = nam
            if not test:
                pass
                parts.append(part)

        #stl inclusion ones
        ps = []
        p = {}
        p["magnet_shape"] = "import"
        p["shape_full"] = "import"
        p["shape_file"] ="working.stl"
        p["width"] = 3
        p["height"] = 1
        p["thickness"] = 3
        p["filename"] = "cylinder_test"
        ps.append(p)

        p = copy.deepcopy(p)
        #filename unicorn_test
        p["filename"] = "unicorn_test"
        ps.append(p)
        

        for p in ps:
            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            p3.update(p)
            filename = p3["filename"]           
            p3["extra"] = f"{filename}_filename"
            part["kwargs"] = p3
            nam = f"magnet_holder_handle"
            part["name"] = nam
            if oomp_mode == "oobb":
                p3["oomp_size"] = nam
            if not test:
                pass
                parts.append(part)


    kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        sort.append("name")
        sort.append("magnet")        
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        sort.append("message")
        #sort.append("extra")
        
        scad_help.generate_navigation(sort = sort)


def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


def get_magnet_holder(thing, **kwargs):
    magnet_shape = kwargs.get("magnet_shape", "cylinder")
    if magnet_shape == "cylinder":
        return get_magnet_holder_cylinder(thing, **kwargs)
    elif magnet_shape == "rectangle":
        return get_magnet_holder_rectangle(thing, **kwargs)



def get_magnet_holder_cylinder(thing, **kwargs):
    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #magnet
    magnet_diameter = kwargs.get("magnet_diameter", 6)
    magnet_depth = kwargs.get("magnet_depth", 6)
    magnet_multiple = kwargs.get("magnet_multiple", 1)
    magnet_offset = kwargs.get("magnet_offset", 7.5)

    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["radius_name"] = "m3"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = ["top","bottom"]
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add magnet holes
    if True:
        extra = 0.25
        magnet_diameter = kwargs.get("magnet_diameter", 6)
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cylinder"
        dep = magnet_depth + extra
        p3["depth"] = dep
        p3["radius"] = (magnet_diameter + extra)/2
        for i in range(magnet_multiple):
            p4 = copy.deepcopy(p3)
            pos1 = copy.deepcopy(pos)         
            pos1[0] += (i - (magnet_multiple-1)/2) * magnet_offset
            pos1[2] += dep /2
            p4["pos"] = pos1
            p4["m"] = "#"
            oobb_base.append_full(thing,**p4)

    #add counter sunk screws on side
    if True:    
        counter_sunk_extra = 0.5
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["depth"] = depth - counter_sunk_extra
        p3["radius_name"] = "m3"
        p3["clearance"] = "top"
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth - counter_sunk_extra
        poss = []
        pos11 = copy.deepcopy(pos1)
        pos11[0] += (width-1)/2 * 15
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -(width-1)/2 * 15
        poss.append(pos12)
        p3["pos"] = poss
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_magnet_holder_handle(thing, **kwargs):
    magnet_shape = kwargs.get("magnet_shape", "cylinder")
    if magnet_shape == "cylinder":
        return get_magnet_holder_handle_cylinder(thing, **kwargs)
    elif magnet_shape == "import":
        return get_magnet_holder_handle_import(thing, **kwargs)
    



def get_magnet_holder_handle_cylinder(thing, **kwargs):
    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    message = kwargs.get("message", "")

    #shape
    shape = kwargs.get("shape", "oobb_cylinder")
    shape_radius = kwargs.get("shape_radius", 15)
    shape_depth = kwargs.get("shape_depth", 6)

    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["radius_name"] = "m3"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = ["top","bottom"]
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add piece
    if True:
        if shape == "oobb_cylinder":
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "positive"
            p3["shape"] = f"oobb_cylinder"
            dep = shape_depth
            p3["depth"] = dep
            p3["radius"] = shape_radius
            pos1 = copy.deepcopy(pos)         
            pos1[0] += 0
            pos1[2] += dep /2
            p3["pos"] = pos1
            #p3["m"] = "#"
            oobb_base.append_full(thing,**p3)

    #add message
    if True:
        if message != "":            
            message_length = len(message)
            text_size_one = 18
            text_size_scale = 1.25


            text_size = text_size_one * 1/message_length * text_size_scale
            

            style = "negative"
            dep = 2
            siz = text_size
            scale_factor = .9
            shift_y = 0#text_size/5.5 * 4 * scale_factor
            p3 = copy.deepcopy(kwargs)
            p3["type"] = style
            p3["shape"] = f"oobb_text"
            p3["text"] = message
            p3["depth"] = dep
            p3["size"] = siz
            p3["font"] = "Arial:Bold"
            p3["center"] = True
            p3["m"] = "#"
            pos1 = copy.deepcopy(pos)
            pos1[0] += -0
            pos1[1] += shift_y
            pos1[2] += depth - dep
            p3["pos"] = pos1
            oobb_base.append_full(thing,**p3)
            

    #add counter sunk screws on side
    if True:    
        counter_sunk_extra = 0.5
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        dep = 20
        p3["depth"] = dep + depth
        p3["radius_name"] = "m3"
        p3["nut"] = True

        if True:        
            pos1 = copy.deepcopy(pos)
            pos1[2] += -dep
            poss = []
            pos11 = copy.deepcopy(pos1)
            pos11[0] += (width-1)/2 * 15
            poss.append(pos11)
            pos12 = copy.deepcopy(pos1)
            pos12[0] += -(width-1)/2 * 15
            poss.append(pos12)
            p3["pos"] = poss
        p3["m"] = "#"
        rot1 = copy.deepcopy(rot)
        rot1[1] += 180
        p3["rot"] = rot1
        oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_magnet_holder_handle_import(thing, **kwargs):
    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    message = kwargs.get("message", "")

    #import
    shape_file_source = kwargs.get("shape_file", "source_files/cylinder_test/working.stl")
    #just_filename of source    
    shape_file = os.path.basename(shape_file_source)    


    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["radius_name"] = "m3"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = ["top","bottom"]
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add piece
    if True:        
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"import_stl"
        p3["file"] = shape_file_source
        pos1 = copy.deepcopy(pos)         
        pos1[0] += 0
        pos1[2] += 0
        p3["pos"] = pos1
        p3["m"] = "#"
        #oobb_base.append_full(thing,**p3)

            

    #add counter sunk screws on side
    if True:    
        counter_sunk_extra = 0.5
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        dep = 20
        p3["depth"] = dep + depth
        p3["radius_name"] = "m3"
        p3["nut"] = True

        if True:        
            pos1 = copy.deepcopy(pos)
            pos1[2] += -dep
            poss = []
            pos11 = copy.deepcopy(pos1)
            pos11[0] += (width-1)/2 * 15
            poss.append(pos11)
            pos12 = copy.deepcopy(pos1)
            pos12[0] += -(width-1)/2 * 15
            poss.append(pos12)
            p3["pos"] = poss
        p3["m"] = "#"
        rot1 = copy.deepcopy(rot)
        rot1[1] += 180
        p3["rot"] = rot1
        oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_magnet_holder_rectangle(thing, **kwargs):
    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    
    #magnet
    magnet_length = kwargs.get("magnet_length", 29)
    magnet_width = kwargs.get("magnet_width", 9.5)
    magnet_depth = kwargs.get("magnet_depth", 6)
    magnet_multiple_x = kwargs.get("magnet_multiple_x", 1)
    magnet_offset_x = kwargs.get("magnet_offset_x", 7.5)
    magnet_multiple_y = kwargs.get("magnet_multiple_y", 1)
    magnet_offset_y = kwargs.get("magnet_offset_y", 7.5)

    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["radius_name"] = "m3"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = ["top","bottom"]
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add magnet holes
    if True:
        extra = 0.25
        magnet_diameter = kwargs.get("magnet_diameter", 6)
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        wid = magnet_length + extra
        dep = magnet_depth + extra
        hei = magnet_width + extra
        size = [wid,hei,dep]
        p3["size"] = size        
        for xx in range(magnet_multiple_x):
            for yy in range(magnet_multiple_y):
                p4 = copy.deepcopy(p3)
                pos1 = copy.deepcopy(pos)         
                pos1[0] += (xx - (magnet_multiple_x-1)/2) * magnet_offset_x
                pos1[1] += (yy - (magnet_multiple_y-1)/2) * magnet_offset_y
                p4["pos"] = pos1
                p4["m"] = "#"
                oobb_base.append_full(thing,**p4)

    #add counter sunk screws on side
    if True:    
        counter_sunk_extra = 0.5
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["depth"] = depth - counter_sunk_extra
        p3["radius_name"] = "m3"
        p3["clearance"] = "top"
        pos1 = copy.deepcopy(pos)
        pos1[2] += depth - counter_sunk_extra
        poss = []
        pos11 = copy.deepcopy(pos1)
        pos11[0] += (width-1)/2 * 15
        poss.append(pos11)
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -(width-1)/2 * 15
        poss.append(pos12)
        p3["pos"] = poss
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)