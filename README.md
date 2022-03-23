# zmap
 An interactive fiction mapper

 zmap is an easy, text-driven mapping application for interactive fiction. Maps are input using a simple domain-specific language.
 
 ## Releases
 
 ~[v1.0.0 for Mac]~ Unavailable for now as I can't get the installer properly signed. So run it from source for now.
 
 __If anyone out there would be willing to package zmap for Windows and/or Linux, let me know at rileypb@gmail.com__
 
 ## zmap code
 Here's how to input a map: (if you want, have a look at the [Antlr grammar](https://github.com/rileypb/zmap/blob/main/src/main/python/zmap.g4).)
 
 A single zmap file can contain multiple maps. A map is indicated by a name followed by `{ ... }` containing the locations and connections on the map.
 
 For example,
 
 ```
 outside_house {
[West of House]n<->w[North of House]
[West of House]s<->w[South of House]
[North of House]n-->*(Forest Path)
[North of House]e<->n[Behind House]
[Behind House]e-->*(Small Clearing)
[Behind House]s<->e[South of House]
[West of House]w-->*(Forest sunlight)
[South of House]s-->*(Forest lantern)
}
house {
[Kitchen]u-->?
[Kitchen]w<->[Living Room]<
[Kitchen]d-->?
[Kitchen]e-->*(Behind House)<

[Living Room]w-->*(Front Door)<
[Living Room]d-->*(Cellar)
}
 ```
 A node with a fixed position on the screen is indicated by square brackets; for example, `[West of House]`. A node that should swing freely is indicated by parens: `(North of House)`.  
 
 An arrow pointing in one direction (`-->` or `<--`) indicates a one-way connection. A two-headed arrow (`<->`) indicates a two-way connection. An arrow is preceded by the direction of the connection (i.e., which way it leaves the originating location). For instance `e-->` indicates a one-way connection pointing east, `e<->` indicates a two-way passage leading east from the originating location and leading west from the target location. A two-way passage may indicate different directions on the two ends: `[West of House]n<->w[North of House]`.
 
 The right side of a right-pointing one-way arrow may indicate an unknown location `([Kitchen]u-->?)`, or a special feature: `[Living Room]w-->*[Front Door]`. Special features are good for transitions between areas, for example.
 
 There are two modifiers which may be appended to a connection: `<` and `>`, which indicate a shorter or longer line on the map, respectively.
 
 ![Outside the House](https://github.com/rileypb/zmap/blob/main/example_map.png)
 
