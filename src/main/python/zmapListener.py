# Generated from /Users/rileypb/dev/zmap/src/main/python/zmap.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .zmapParser import zmapParser
else:
    from zmapParser import zmapParser

from map import *


# This class defines a complete listener for a parse tree produced by zmapParser.
class zmapListener(ParseTreeListener):

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
        pass

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
        pass

    # Exit a parse tree produced by zmapParser#passage.
    def exitPassage(self, ctx:zmapParser.PassageContext):
        pass


    # Enter a parse tree produced by zmapParser#comment.
    def enterComment(self, ctx:zmapParser.CommentContext):
        pass

    # Exit a parse tree produced by zmapParser#comment.
    def exitComment(self, ctx:zmapParser.CommentContext):
        pass


    # Enter a parse tree produced by zmapParser#room.
    def enterRoom(self, ctx:zmapParser.RoomContext):
        pass

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
        pass


    # Enter a parse tree produced by zmapParser#special.
    def enterSpecial(self, ctx:zmapParser.SpecialContext):
        pass

    # Exit a parse tree produced by zmapParser#special.
    def exitSpecial(self, ctx:zmapParser.SpecialContext):
        pass



del zmapParser