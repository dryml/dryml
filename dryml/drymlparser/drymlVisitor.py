from antlr4 import *

if __name__ is not None and "." in __name__:
    from .drymlParser import drymlParser
else:
    from drymlParser import drymlParser


# This class defines a complete generic visitor for a parse tree produced by drymlParser.


class drymlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by drymlParser#file_input.
    def visitFile_input(self, ctx: drymlParser.File_inputContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#stmt.
    def visitStmt(self, ctx: drymlParser.StmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#actordef.
    def visitActordef(self, ctx: drymlParser.ActordefContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#actor_id.
    def visitActor_id(self, ctx: drymlParser.Actor_idContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#actor_name.
    def visitActor_name(self, ctx: drymlParser.Actor_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resourcedef.
    def visitResourcedef(self, ctx: drymlParser.ResourcedefContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resource_id.
    def visitResource_id(self, ctx: drymlParser.Resource_idContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resource_name.
    def visitResource_name(self, ctx: drymlParser.Resource_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resource_body.
    def visitResource_body(self, ctx: drymlParser.Resource_bodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resource_states.
    def visitResource_states(self, ctx: drymlParser.Resource_statesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resource_states_list.
    def visitResource_states_list(self, ctx: drymlParser.Resource_states_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resource_state_def.
    def visitResource_state_def(self, ctx: drymlParser.Resource_state_defContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resource_state_id.
    def visitResource_state_id(self, ctx: drymlParser.Resource_state_idContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resource_state_name.
    def visitResource_state_name(self, ctx: drymlParser.Resource_state_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resource_parameters.
    def visitResource_parameters(self, ctx: drymlParser.Resource_parametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resource_parameters_list.
    def visitResource_parameters_list(
            self, ctx: drymlParser.Resource_parameters_listContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resource_parameter_def.
    def visitResource_parameter_def(
            self, ctx: drymlParser.Resource_parameter_defContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resource_parameter_id.
    def visitResource_parameter_id(self, ctx: drymlParser.Resource_parameter_idContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#resource_parameter_name.
    def visitResource_parameter_name(
            self, ctx: drymlParser.Resource_parameter_nameContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#activitydef.
    def visitActivitydef(self, ctx: drymlParser.ActivitydefContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#actor_a_id.
    def visitActor_a_id(self, ctx: drymlParser.Actor_a_idContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#actor_b_id.
    def visitActor_b_id(self, ctx: drymlParser.Actor_b_idContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#control_flow_type.
    def visitControl_flow_type(self, ctx: drymlParser.Control_flow_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#activity_id.
    def visitActivity_id(self, ctx: drymlParser.Activity_idContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#activity_name.
    def visitActivity_name(self, ctx: drymlParser.Activity_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#activity_body.
    def visitActivity_body(self, ctx: drymlParser.Activity_bodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#input_resources.
    def visitInput_resources(self, ctx: drymlParser.Input_resourcesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#input_resources_list.
    def visitInput_resources_list(self, ctx: drymlParser.Input_resources_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#input_resource_body.
    def visitInput_resource_body(self, ctx: drymlParser.Input_resource_bodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#input_resource_id.
    def visitInput_resource_id(self, ctx: drymlParser.Input_resource_idContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#input_resource_state_id.
    def visitInput_resource_state_id(
            self, ctx: drymlParser.Input_resource_state_idContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#input_resource_parameters_body.
    def visitInput_resource_parameters_body(
            self, ctx: drymlParser.Input_resource_parameters_bodyContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#input_resource_parameters.
    def visitInput_resource_parameters(
            self, ctx: drymlParser.Input_resource_parametersContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#input_resource_parameter_body.
    def visitInput_resource_parameter_body(
            self, ctx: drymlParser.Input_resource_parameter_bodyContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#input_resource_parameter_id.
    def visitInput_resource_parameter_id(
            self, ctx: drymlParser.Input_resource_parameter_idContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#input_resource_parameter_value.
    def visitInput_resource_parameter_value(
            self, ctx: drymlParser.Input_resource_parameter_valueContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#output_resources.
    def visitOutput_resources(self, ctx: drymlParser.Output_resourcesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#output_resources_list.
    def visitOutput_resources_list(self, ctx: drymlParser.Output_resources_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#output_resource_body.
    def visitOutput_resource_body(self, ctx: drymlParser.Output_resource_bodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#output_resource_id.
    def visitOutput_resource_id(self, ctx: drymlParser.Output_resource_idContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#output_resource_state_id.
    def visitOutput_resource_state_id(
            self, ctx: drymlParser.Output_resource_state_idContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#output_resource_parameters_body.
    def visitOutput_resource_parameters_body(
            self, ctx: drymlParser.Output_resource_parameters_bodyContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#output_resource_parameters.
    def visitOutput_resource_parameters(
            self, ctx: drymlParser.Output_resource_parametersContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#output_resource_parameter_body.
    def visitOutput_resource_parameter_body(
            self, ctx: drymlParser.Output_resource_parameter_bodyContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#output_resource_parameter_id.
    def visitOutput_resource_parameter_id(
            self, ctx: drymlParser.Output_resource_parameter_idContext
    ):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by drymlParser#output_resource_parameter_value.
    def visitOutput_resource_parameter_value(
            self, ctx: drymlParser.Output_resource_parameter_valueContext
    ):
        return self.visitChildren(ctx)


del drymlParser
