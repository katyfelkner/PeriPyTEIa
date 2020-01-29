# class for text containing elements of TEI text

import xml.etree.ElementTree as ETree


class TextContainingElement(ETree.Element):
    def __init__(self, tag, **extra):
        # for the superclass, tag is set by caller
        # here, tag will be passed in by the caller (i.e. the parser)
        # then passed out to the superclass constructor

        super().__init__(tag, **extra)

        # initialize text children
        text_children = []
        # initialize non text children
        non_text_children = []

        # these lists will be populated by the parser

    def __getitem__(self, item):
        return self.text_children[item]

    def __setitem__(self, key, value):
        # TODO: what exactly should this do?
        pass

    def text(self):
        textstr = ""
        # TODO: how to get the text and non text in the right order?
        # Options:
            # maintain one long list of children and mark them text/nontext
            # try to use underlying etree structure
                # this is more sound from a SWE perspective, but I am not sure how to do it
                # iterate over children of the e tree element anc check the type of each?
                # but we don't have access to the subclass object if we do that....
                # what we need is to create a tree of TE, TCE, and NTE

        return textstr


    # TODO: should there be a parse method in this class?
    # should parsing be recursive or iterative?
