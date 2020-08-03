from antlr4 import *

if __name__ is not None and "." in __name__:
    from .drymlParser import drymlParser
else:
    from drymlParser import drymlParser


# This class defines a complete listener for a parse tree produced by drymlParser.
class drymlListener(ParseTreeListener):

    # Enter a parse tree produced by drymlParser#file_input.
    def enterFile_input(self, ctx: drymlParser.File_inputContext):
        pass

    # Exit a parse tree produced by drymlParser#file_input.
    def exitFile_input(self, ctx: drymlParser.File_inputContext):
        pass

    # Enter a parse tree produced by drymlParser#stmt.
    def enterStmt(self, ctx: drymlParser.StmtContext):
        pass

    # Exit a parse tree produced by drymlParser#stmt.
    def exitStmt(self, ctx: drymlParser.StmtContext):
        pass

    # Enter a parse tree produced by drymlParser#actordef.
    def enterActordef(self, ctx: drymlParser.ActordefContext):
        pass

    # Exit a parse tree produced by drymlParser#actordef.
    def exitActordef(self, ctx: drymlParser.ActordefContext):
        pass

    # Enter a parse tree produced by drymlParser#actor_id.
    def enterActor_id(self, ctx: drymlParser.Actor_idContext):
        pass

    # Exit a parse tree produced by drymlParser#actor_id.
    def exitActor_id(self, ctx: drymlParser.Actor_idContext):
        pass

    # Enter a parse tree produced by drymlParser#actor_name.
    def enterActor_name(self, ctx: drymlParser.Actor_nameContext):
        pass

    # Exit a parse tree produced by drymlParser#actor_name.
    def exitActor_name(self, ctx: drymlParser.Actor_nameContext):
        pass

    # Enter a parse tree produced by drymlParser#resourcedef.
    def enterResourcedef(self, ctx: drymlParser.ResourcedefContext):
        pass

    # Exit a parse tree produced by drymlParser#resourcedef.
    def exitResourcedef(self, ctx: drymlParser.ResourcedefContext):
        pass

    # Enter a parse tree produced by drymlParser#resource_id.
    def enterResource_id(self, ctx: drymlParser.Resource_idContext):
        pass

    # Exit a parse tree produced by drymlParser#resource_id.
    def exitResource_id(self, ctx: drymlParser.Resource_idContext):
        pass

    # Enter a parse tree produced by drymlParser#resource_name.
    def enterResource_name(self, ctx: drymlParser.Resource_nameContext):
        pass

    # Exit a parse tree produced by drymlParser#resource_name.
    def exitResource_name(self, ctx: drymlParser.Resource_nameContext):
        pass

    # Enter a parse tree produced by drymlParser#resource_body.
    def enterResource_body(self, ctx: drymlParser.Resource_bodyContext):
        pass

    # Exit a parse tree produced by drymlParser#resource_body.
    def exitResource_body(self, ctx: drymlParser.Resource_bodyContext):
        pass

    # Enter a parse tree produced by drymlParser#resource_states.
    def enterResource_states(self, ctx: drymlParser.Resource_statesContext):
        pass

    # Exit a parse tree produced by drymlParser#resource_states.
    def exitResource_states(self, ctx: drymlParser.Resource_statesContext):
        pass

    # Enter a parse tree produced by drymlParser#resource_states_list.
    def enterResource_states_list(self, ctx: drymlParser.Resource_states_listContext):
        pass

    # Exit a parse tree produced by drymlParser#resource_states_list.
    def exitResource_states_list(self, ctx: drymlParser.Resource_states_listContext):
        pass

    # Enter a parse tree produced by drymlParser#resource_state_def.
    def enterResource_state_def(self, ctx: drymlParser.Resource_state_defContext):
        pass

    # Exit a parse tree produced by drymlParser#resource_state_def.
    def exitResource_state_def(self, ctx: drymlParser.Resource_state_defContext):
        pass

    # Enter a parse tree produced by drymlParser#resource_state_id.
    def enterResource_state_id(self, ctx: drymlParser.Resource_state_idContext):
        pass

    # Exit a parse tree produced by drymlParser#resource_state_id.
    def exitResource_state_id(self, ctx: drymlParser.Resource_state_idContext):
        pass

    # Enter a parse tree produced by drymlParser#resource_state_name.
    def enterResource_state_name(self, ctx: drymlParser.Resource_state_nameContext):
        pass

    # Exit a parse tree produced by drymlParser#resource_state_name.
    def exitResource_state_name(self, ctx: drymlParser.Resource_state_nameContext):
        pass

    # Enter a parse tree produced by drymlParser#resource_parameters.
    def enterResource_parameters(self, ctx: drymlParser.Resource_parametersContext):
        pass

    # Exit a parse tree produced by drymlParser#resource_parameters.
    def exitResource_parameters(self, ctx: drymlParser.Resource_parametersContext):
        pass

    # Enter a parse tree produced by drymlParser#resource_parameters_list.
    def enterResource_parameters_list(
            self, ctx: drymlParser.Resource_parameters_listContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#resource_parameters_list.
    def exitResource_parameters_list(
            self, ctx: drymlParser.Resource_parameters_listContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#resource_parameter_def.
    def enterResource_parameter_def(
            self, ctx: drymlParser.Resource_parameter_defContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#resource_parameter_def.
    def exitResource_parameter_def(
            self, ctx: drymlParser.Resource_parameter_defContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#resource_parameter_id.
    def enterResource_parameter_id(self, ctx: drymlParser.Resource_parameter_idContext):
        pass

    # Exit a parse tree produced by drymlParser#resource_parameter_id.
    def exitResource_parameter_id(self, ctx: drymlParser.Resource_parameter_idContext):
        pass

    # Enter a parse tree produced by drymlParser#resource_parameter_name.
    def enterResource_parameter_name(
            self, ctx: drymlParser.Resource_parameter_nameContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#resource_parameter_name.
    def exitResource_parameter_name(
            self, ctx: drymlParser.Resource_parameter_nameContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#activitydef.
    def enterActivitydef(self, ctx: drymlParser.ActivitydefContext):
        pass

    # Exit a parse tree produced by drymlParser#activitydef.
    def exitActivitydef(self, ctx: drymlParser.ActivitydefContext):
        pass

    # Enter a parse tree produced by drymlParser#actor_a_id.
    def enterActor_a_id(self, ctx: drymlParser.Actor_a_idContext):
        pass

    # Exit a parse tree produced by drymlParser#actor_a_id.
    def exitActor_a_id(self, ctx: drymlParser.Actor_a_idContext):
        pass

    # Enter a parse tree produced by drymlParser#actor_b_id.
    def enterActor_b_id(self, ctx: drymlParser.Actor_b_idContext):
        pass

    # Exit a parse tree produced by drymlParser#actor_b_id.
    def exitActor_b_id(self, ctx: drymlParser.Actor_b_idContext):
        pass

    # Enter a parse tree produced by drymlParser#control_flow_type.
    def enterControl_flow_type(self, ctx: drymlParser.Control_flow_typeContext):
        pass

    # Exit a parse tree produced by drymlParser#control_flow_type.
    def exitControl_flow_type(self, ctx: drymlParser.Control_flow_typeContext):
        pass

    # Enter a parse tree produced by drymlParser#activity_id.
    def enterActivity_id(self, ctx: drymlParser.Activity_idContext):
        pass

    # Exit a parse tree produced by drymlParser#activity_id.
    def exitActivity_id(self, ctx: drymlParser.Activity_idContext):
        pass

    # Enter a parse tree produced by drymlParser#activity_name.
    def enterActivity_name(self, ctx: drymlParser.Activity_nameContext):
        pass

    # Exit a parse tree produced by drymlParser#activity_name.
    def exitActivity_name(self, ctx: drymlParser.Activity_nameContext):
        pass

    # Enter a parse tree produced by drymlParser#activity_body.
    def enterActivity_body(self, ctx: drymlParser.Activity_bodyContext):
        pass

    # Exit a parse tree produced by drymlParser#activity_body.
    def exitActivity_body(self, ctx: drymlParser.Activity_bodyContext):
        pass

    # Enter a parse tree produced by drymlParser#input_resources.
    def enterInput_resources(self, ctx: drymlParser.Input_resourcesContext):
        pass

    # Exit a parse tree produced by drymlParser#input_resources.
    def exitInput_resources(self, ctx: drymlParser.Input_resourcesContext):
        pass

    # Enter a parse tree produced by drymlParser#input_resources_list.
    def enterInput_resources_list(self, ctx: drymlParser.Input_resources_listContext):
        pass

    # Exit a parse tree produced by drymlParser#input_resources_list.
    def exitInput_resources_list(self, ctx: drymlParser.Input_resources_listContext):
        pass

    # Enter a parse tree produced by drymlParser#input_resource_body.
    def enterInput_resource_body(self, ctx: drymlParser.Input_resource_bodyContext):
        pass

    # Exit a parse tree produced by drymlParser#input_resource_body.
    def exitInput_resource_body(self, ctx: drymlParser.Input_resource_bodyContext):
        pass

    # Enter a parse tree produced by drymlParser#input_resource_id.
    def enterInput_resource_id(self, ctx: drymlParser.Input_resource_idContext):
        pass

    # Exit a parse tree produced by drymlParser#input_resource_id.
    def exitInput_resource_id(self, ctx: drymlParser.Input_resource_idContext):
        pass

    # Enter a parse tree produced by drymlParser#input_resource_state_id.
    def enterInput_resource_state_id(
            self, ctx: drymlParser.Input_resource_state_idContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#input_resource_state_id.
    def exitInput_resource_state_id(
            self, ctx: drymlParser.Input_resource_state_idContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#input_resource_parameters_body.
    def enterInput_resource_parameters_body(
            self, ctx: drymlParser.Input_resource_parameters_bodyContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#input_resource_parameters_body.
    def exitInput_resource_parameters_body(
            self, ctx: drymlParser.Input_resource_parameters_bodyContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#input_resource_parameters.
    def enterInput_resource_parameters(
            self, ctx: drymlParser.Input_resource_parametersContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#input_resource_parameters.
    def exitInput_resource_parameters(
            self, ctx: drymlParser.Input_resource_parametersContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#input_resource_parameter_body.
    def enterInput_resource_parameter_body(
            self, ctx: drymlParser.Input_resource_parameter_bodyContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#input_resource_parameter_body.
    def exitInput_resource_parameter_body(
            self, ctx: drymlParser.Input_resource_parameter_bodyContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#input_resource_parameter_id.
    def enterInput_resource_parameter_id(
            self, ctx: drymlParser.Input_resource_parameter_idContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#input_resource_parameter_id.
    def exitInput_resource_parameter_id(
            self, ctx: drymlParser.Input_resource_parameter_idContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#input_resource_parameter_value.
    def enterInput_resource_parameter_value(
            self, ctx: drymlParser.Input_resource_parameter_valueContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#input_resource_parameter_value.
    def exitInput_resource_parameter_value(
            self, ctx: drymlParser.Input_resource_parameter_valueContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#output_resources.
    def enterOutput_resources(self, ctx: drymlParser.Output_resourcesContext):
        pass

    # Exit a parse tree produced by drymlParser#output_resources.
    def exitOutput_resources(self, ctx: drymlParser.Output_resourcesContext):
        pass

    # Enter a parse tree produced by drymlParser#output_resources_list.
    def enterOutput_resources_list(self, ctx: drymlParser.Output_resources_listContext):
        pass

    # Exit a parse tree produced by drymlParser#output_resources_list.
    def exitOutput_resources_list(self, ctx: drymlParser.Output_resources_listContext):
        pass

    # Enter a parse tree produced by drymlParser#output_resource_body.
    def enterOutput_resource_body(self, ctx: drymlParser.Output_resource_bodyContext):
        pass

    # Exit a parse tree produced by drymlParser#output_resource_body.
    def exitOutput_resource_body(self, ctx: drymlParser.Output_resource_bodyContext):
        pass

    # Enter a parse tree produced by drymlParser#output_resource_id.
    def enterOutput_resource_id(self, ctx: drymlParser.Output_resource_idContext):
        pass

    # Exit a parse tree produced by drymlParser#output_resource_id.
    def exitOutput_resource_id(self, ctx: drymlParser.Output_resource_idContext):
        pass

    # Enter a parse tree produced by drymlParser#output_resource_state_id.
    def enterOutput_resource_state_id(
            self, ctx: drymlParser.Output_resource_state_idContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#output_resource_state_id.
    def exitOutput_resource_state_id(
            self, ctx: drymlParser.Output_resource_state_idContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#output_resource_parameters_body.
    def enterOutput_resource_parameters_body(
            self, ctx: drymlParser.Output_resource_parameters_bodyContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#output_resource_parameters_body.
    def exitOutput_resource_parameters_body(
            self, ctx: drymlParser.Output_resource_parameters_bodyContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#output_resource_parameters.
    def enterOutput_resource_parameters(
            self, ctx: drymlParser.Output_resource_parametersContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#output_resource_parameters.
    def exitOutput_resource_parameters(
            self, ctx: drymlParser.Output_resource_parametersContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#output_resource_parameter_body.
    def enterOutput_resource_parameter_body(
            self, ctx: drymlParser.Output_resource_parameter_bodyContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#output_resource_parameter_body.
    def exitOutput_resource_parameter_body(
            self, ctx: drymlParser.Output_resource_parameter_bodyContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#output_resource_parameter_id.
    def enterOutput_resource_parameter_id(
            self, ctx: drymlParser.Output_resource_parameter_idContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#output_resource_parameter_id.
    def exitOutput_resource_parameter_id(
            self, ctx: drymlParser.Output_resource_parameter_idContext
    ):
        pass

    # Enter a parse tree produced by drymlParser#output_resource_parameter_value.
    def enterOutput_resource_parameter_value(
            self, ctx: drymlParser.Output_resource_parameter_valueContext
    ):
        pass

    # Exit a parse tree produced by drymlParser#output_resource_parameter_value.
    def exitOutput_resource_parameter_value(
            self, ctx: drymlParser.Output_resource_parameter_valueContext
    ):
        pass


del drymlParser
