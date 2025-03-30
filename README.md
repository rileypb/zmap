# Note: zmap has been superseded by [zmap_cli](https://github.com/rileypb/zmap_cli).

# zmap
 An interactive fiction mapper

 zmap is an easy, text-driven mapping application for interactive fiction. Maps are input using a simple domain-specific language.
 
 ## Releases
 
 ~[v1.0.0 for Mac]~ Unavailable for now as I can't get the installer properly signed. So run it from source for now.
 
 __If anyone out there would be willing to package zmap for Windows and/or Linux, let me know at rileypb@gmail.com__
 
 ## zmap code
 Here's how to input a map: (if you want, have a look at the [Antlr grammar](https://github.com/rileypb/zmap/blob/main/src/main/python/zmap.g4).) The grammar is a modified [graphviz DOT grammar](https://graphviz.org/doc/info/lang.html)
 
 A single zmap file can contain multiple maps. A map is indicated by a name followed by `{ ... }` containing the locations and connections on the map.
 
 For example,
 
 ```
outside_house {
West_of_House:n<->w:North_of_House
West_of_House:s<->w:South_of_House
North_of_House:n-->Forest_Path*
North_of_House:e<->n:Behind_House
Behind_House:e-->Small_Clearing*
Behind_House:s<->e:South_of_House
West_of_House:w-->Forest_sunlight*
South_of_House:s-->Forest_lantern*
}
house {
Attic [dark]

Kitchen:u<->Attic [short]
Kitchen:w<->Living_Room [short]
Kitchen:d-->"Can't climb down chimney"*
Kitchen:e-->Behind_House* [short]
Living_Room:w-->Front_Door* [short]
Living_Room:d-->Cellar* [short]
}
 ```

Passages are of the form `West_of_House:n<->w:North_of_House`, where `West_of_House` and `North_of_House` are rooms, `n` and `w` are the directions the passage leaves each room, and `<->` indicates the passage goes both ways. Passages can also be one-way: `-->`.

When declaring a two-way passage, the direction on the right side of the arrows need not be specified: `East_West_Passage:e<->Round_Room`. In this case the right-hand direction is assumed to be the opposite of the left-hand direction.

Rooms are implicitly declared when mentioned in passage definitions.

Passages can have properties, listed in square brackets: `Kitchen:u<->Attic [short]`. This indicates the passage should be drawn at half the usual length, if possible. The complementary property `long` is also available.

An asterisk indicates a "special": `Kitchen:d-->"Can't climb down chimney"*`. This is handy for indicating directions that cannot be traveled in.

Room names should use underscores to indicate spaces. This limitation can be avoided by surrounding the room name with double quotes. Without quotes the character set is limited to alphanumeric characters and underscores. In quotes, this restriction is lifted.

Room properties can be listed like so: `Attic [dark]`.

Map properties can be listed like so: `graph [splines]`. This property indicates that passages should be drawn using splines. 

Splines can be turned off and on per passage using the values `never`, `always`, and `inherit`. For instance `East_of_Chasm:e<->Gallery [splines=never]`. The default value is `inherit`. 

Unknown locations may be indicated thusly: `Dam:d-->?`. Two-way passages cannot be used with unknown locations. One can indicate unknown locations that are known to be dark: `Gallery:n-->!`


 
 ![Outside the House](https://github.com/rileypb/zmap/blob/main/example_map.png)
 
