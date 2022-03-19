# Generated from /Users/rileypb/dev/zmap/src/zmap.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .zmapParser import zmapParser
else:
    from zmapParser import zmapParser

from map import *



opposites = { 'n': 's', 'ne': 'sw', 'e': 'w', 'se': 'nw', 's': 'n', 'sw': 'ne',
              'w': 'e', 'nw': 'se', 'u': 'd', 'd': 'u'}

def opposite(direction):
    return opposites[direction]

# This class defines a complete listener for a parse tree produced by zmapParser.
class zmapListenerImpl(ParseTreeListener):

    def __init__(self):
        self.new_maps = {}

    # Enter a parse tree produced by zmapParser#parse.
    def enterParse(self, ctx:zmapParser.ParseContext):
        pass

    # Exit a parse tree produced by zmapParser#parse.
    def exitParse(self, ctx:zmapParser.ParseContext):
        pass


    # Enter a parse tree produced by zmapParser#ifmaps.
    def enterIfmaps(self, ctx:zmapParser.IfmapsContext):
        pass

    # Exit a parse tree produced by zmapParser#ifmaps.
    def exitIfmaps(self, ctx:zmapParser.IfmapsContext):
        pass


    # Enter a parse tree produced by zmapParser#ifmapblock.
    def enterIfmapblock(self, ctx:zmapParser.IfmapblockContext):
        name = ctx.name().getText()
        self.new_map = Map()
        self.new_maps[name] = self.new_map

    # Exit a parse tree produced by zmapParser#ifmapblock.
    def exitIfmapblock(self, ctx:zmapParser.IfmapblockContext):
        pass


    # Enter a parse tree produced by zmapParser#ifmap.
    def enterIfmap(self, ctx:zmapParser.IfmapContext):
        pass

    # Exit a parse tree produced by zmapParser#ifmap.
    def exitIfmap(self, ctx:zmapParser.IfmapContext):
        pass


    # Enter a parse tree produced by zmapParser#passage.
    def enterPassage(self, ctx:zmapParser.PassageContext):
        self.room1 = None
        self.room2 = None

    # Exit a parse tree produced by zmapParser#passage.
    def exitPassage(self, ctx:zmapParser.PassageContext):
        if not ctx.room():
            return
        room1id = ctx.room()[0].name().getText()
        room1 = self.new_map.rooms[room1id]
        if ctx.unknown():
            room2id = id(ctx.unknown())
        elif ctx.special():
            room2id = id(ctx.special())
        else:
            room2id = ctx.room()[1].name().getText()
        room2 = self.new_map.rooms[room2id]
        modifier_ = ctx.modifier()
        modifier = None if not modifier_ else modifier_.getText()
        if ctx.directed_arrow().larrow():
            print("left")
            direction = ctx.directed_arrow().left_direction().getText()
            self.new_map.add_passage(room1, direction, room2, modifier=modifier)
        elif ctx.directed_arrow().rarrow():
            print("right")
            direction = ctx.directed_arrow().right_direction().getText()
            self.new_map.add_passage(room2, direction, room1, modifier=modifier)
        else: # barrow
            print("both")
            direction1_ = ctx.directed_arrow().left_direction()
            direction1 = direction1_.getText() if direction1_ else None
            direction2_ = ctx.directed_arrow().right_direction()
            direction2 = direction2_.getText() if direction2_ else None
            if not direction1:
                direction1 = opposite(direction2)
            if not direction2:
                direction2 = opposite(direction1)
            print(direction1, direction2)
            self.new_map.add_passage(room1, direction1, to_room=room2, back_direction=direction2, modifier=modifier, two_way=True)




    # Enter a parse tree produced by zmapParser#comment.
    def enterComment(self, ctx:zmapParser.CommentContext):
        pass

    # Exit a parse tree produced by zmapParser#comment.
    def exitComment(self, ctx:zmapParser.CommentContext):
        pass


    # Enter a parse tree produced by zmapParser#room.
    def enterRoom(self, ctx:zmapParser.RoomContext):
        id = ctx.name().getText()
        self.new_map.add_room(id=id, label=id)

    # Exit a parse tree produced by zmapParser#room.
    def exitRoom(self, ctx:zmapParser.RoomContext):
        pass


    # Enter a parse tree produced by zmapParser#modifier.
    def enterModifier(self, ctx:zmapParser.ModifierContext):
        pass

    # Exit a parse tree produced by zmapParser#modifier.
    def exitModifier(self, ctx:zmapParser.ModifierContext):
        pass


    # Enter a parse tree produced by zmapParser#name.
    def enterName(self, ctx:zmapParser.NameContext):
        pass

    # Exit a parse tree produced by zmapParser#name.
    def exitName(self, ctx:zmapParser.NameContext):
        pass


    # Enter a parse tree produced by zmapParser#directed_arrow.
    def enterDirected_arrow(self, ctx:zmapParser.Directed_arrowContext):
        pass

    # Exit a parse tree produced by zmapParser#directed_arrow.
    def exitDirected_arrow(self, ctx:zmapParser.Directed_arrowContext):
        pass
    # Enter a parse tree produced by zmapParser#larrow.
    def enterLarrow(self, ctx:zmapParser.LarrowContext):
        pass

    # Exit a parse tree produced by zmapParser#larrow.
    def exitLarrow(self, ctx:zmapParser.LarrowContext):
        pass


    # Enter a parse tree produced by zmapParser#rarrow.
    def enterRarrow(self, ctx:zmapParser.RarrowContext):
        pass

    # Exit a parse tree produced by zmapParser#rarrow.
    def exitRarrow(self, ctx:zmapParser.RarrowContext):
        pass


    # Enter a parse tree produced by zmapParser#barrow.
    def enterBarrow(self, ctx:zmapParser.BarrowContext):
        pass

    # Exit a parse tree produced by zmapParser#barrow.
    def exitBarrow(self, ctx:zmapParser.BarrowContext):
        pass


    # Enter a parse tree produced by zmapParser#left_direction.
    def enterLeft_direction(self, ctx:zmapParser.Left_directionContext):
        pass

    # Exit a parse tree produced by zmapParser#left_direction.
    def exitLeft_direction(self, ctx:zmapParser.Left_directionContext):
        pass


    # Enter a parse tree produced by zmapParser#right_direction.
    def enterRight_direction(self, ctx:zmapParser.Right_directionContext):
        pass

    # Exit a parse tree produced by zmapParser#right_direction.
    def exitRight_direction(self, ctx:zmapParser.Right_directionContext):
        pass


    # Enter a parse tree produced by zmapParser#arrow.
    def enterArrow(self, ctx:zmapParser.ArrowContext):
        pass

    # Exit a parse tree produced by zmapParser#arrow.
    def exitArrow(self, ctx:zmapParser.ArrowContext):
        pass


    # Enter a parse tree produced by zmapParser#unknown.
    def enterUnknown(self, ctx:zmapParser.UnknownContext):
        pass

    # Exit a parse tree produced by zmapParser#unknown.
    def exitUnknown(self, ctx:zmapParser.UnknownContext):
        self.new_map.add_room(id(ctx), subtype="Unknown")


    # Enter a parse tree produced by zmapParser#special.
    def enterSpecial(self, ctx:zmapParser.SpecialContext):
        pass

    # Exit a parse tree produced by zmapParser#special.
    def exitSpecial(self, ctx:zmapParser.SpecialContext):
        self.new_map.add_room(id(ctx), label=ctx.name().getText(), subtype="Special")



del zmapParser