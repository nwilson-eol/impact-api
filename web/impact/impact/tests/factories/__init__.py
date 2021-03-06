# MIT License
# Copyright (c) 2017 MassChallenge, Inc.

from accelerator.tests.factories.application_answer_factory import (
    ApplicationAnswerFactory
)
from accelerator.tests.factories.application_factory import ApplicationFactory
from accelerator.tests.factories.application_panel_assignment_factory import (
    ApplicationPanelAssignmentFactory,
)
from accelerator.tests.factories.application_question_factory import (
    ApplicationQuestionFactory
)
from accelerator.tests.factories.application_type_factory import (
    ApplicationTypeFactory
)
from accelerator.tests.factories.base_profile_factory import BaseProfileFactory
from accelerator.tests.factories.bucket_state_factory import BucketStateFactory
from accelerator.tests.factories.content_type_factory import ContentTypeFactory
from accelerator.tests.factories.clearance_factory import ClearanceFactory
from accelerator.tests.factories.core_profile_factory import CoreProfileFactory
from accelerator.tests.factories.entrepreneur_factory import (
    EntrepreneurFactory
)
from accelerator.tests.factories.entrepreneur_profile_factory import (
    EntrepreneurProfileFactory
)
from accelerator.tests.factories.expert_category_factory import (
    ExpertCategoryFactory
)
from accelerator.tests.factories.expert_factory import ExpertFactory
from accelerator.tests.factories.expert_interest_type_factory import (
    ExpertInterestTypeFactory
)
from accelerator.tests.factories.expert_profile_factory import (
    ExpertProfileFactory
)
from accelerator.tests.factories.group_factory import GroupFactory
from accelerator.tests.factories.functional_expertise_factory import (
    FunctionalExpertiseFactory
)
from accelerator.tests.factories.industry_factory import IndustryFactory
from accelerator.tests.factories.interest_category_factory import (
    InterestCategoryFactory
)
from accelerator.tests.factories.job_posting_factory import JobPostingFactory
from accelerator.tests.factories.judge_application_feedback_factory import (
    JudgeApplicationFeedbackFactory
)
from accelerator.tests.factories.judge_availability_factory import (
    JudgeAvailabilityFactory
)
from accelerator.tests.factories.judge_feedback_component_factory import (
    JudgeFeedbackComponentFactory
)
from accelerator.tests.factories.judge_panel_assignment_factory import (
    JudgePanelAssignmentFactory
)
from accelerator.tests.factories.judge_round_commitment_factory import (
    JudgeRoundCommitmentFactory
)
from accelerator.tests.factories.judging_form_element_factory import (
    JudgingFormElementFactory
)
from accelerator.tests.factories.judging_form_factory import JudgingFormFactory
from accelerator.tests.factories.judging_round_factory import (
    JudgingRoundFactory
)
from accelerator.tests.factories.member_factory import MemberFactory
from accelerator.tests.factories.member_profile_factory import (
    MemberProfileFactory
)
from accelerator.tests.factories.mentoring_specialties_factory import (
    MentoringSpecialtiesFactory
)
from accelerator.tests.factories.named_group_factory import NamedGroupFactory
from accelerator.tests.factories.newsletter_factory import NewsletterFactory
from accelerator.tests.factories.newsletter_receipt_factory import (
    NewsletterReceiptFactory
)
from accelerator.tests.factories.observer_factory import ObserverFactory
from accelerator.tests.factories.organization_factory import (
    OrganizationFactory
)
from accelerator.tests.factories.panel_factory import PanelFactory
from accelerator.tests.factories.panel_location_factory import (
    PanelLocationFactory
)
from accelerator.tests.factories.panel_time_factory import PanelTimeFactory
from accelerator.tests.factories.panel_type_factory import PanelTypeFactory
from accelerator.tests.factories.partner_factory import PartnerFactory
from accelerator.tests.factories.partner_team_member_factory import (
    PartnerTeamMemberFactory
)
from accelerator.tests.factories.paypal_payment_factory import (
    PayPalPaymentFactory
)
from accelerator.tests.factories.permission_factory import PermissionFactory
from accelerator.tests.factories.program_cycle_factory import (
    ProgramCycleFactory
)
from accelerator.tests.factories.program_factory import ProgramFactory
from accelerator.tests.factories.program_family_factory import (
    ProgramFamilyFactory
)
from accelerator.tests.factories.program_override_factory import (
    ProgramOverrideFactory
)
from accelerator.tests.factories.program_partner_factory import (
    ProgramPartnerFactory
)
from accelerator.tests.factories.program_partner_type_factory import (
    ProgramPartnerTypeFactory
)
from accelerator.tests.factories.program_role_factory import ProgramRoleFactory
from accelerator.tests.factories.program_role_grant_factory import (
    ProgramRoleGrantFactory
)
from accelerator.tests.factories.program_startup_status_factory import (
    ProgramStartupStatusFactory
)
from accelerator.tests.factories.question_factory import QuestionFactory
from accelerator.tests.factories.recommendation_tag_factory import (
    RecommendationTagFactory
)
from accelerator.tests.factories.reference_factory import ReferenceFactory
from accelerator.tests.factories.refund_code_factory import RefundCodeFactory
from accelerator.tests.factories.refund_code_redemption_factory import (
    RefundCodeRedemptionFactory
)
from accelerator.tests.factories.site_factory import SiteFactory
from accelerator.tests.factories.site_program_authorization_factory import (
    SiteProgramAuthorizationFactory
)
from accelerator.tests.factories.scenario_application_factory import (
    ScenarioApplicationFactory
)
from accelerator.tests.factories.scenario_factory import ScenarioFactory
from accelerator.tests.factories.scenario_judge_factory import (
    ScenarioJudgeFactory
)
from accelerator.tests.factories.scenario_preference_factory import (
    ScenarioPreferenceFactory
)
from accelerator.tests.factories.section_factory import SectionFactory
from accelerator.tests.factories.startup_factory import StartupFactory
from accelerator.tests.factories.startup_label_factory import (
    StartupLabelFactory
)
from accelerator.tests.factories.startup_mentor_tracking_record_factory \
    import StartupMentorTrackingRecordFactory
from accelerator.tests.factories.startup_override_grant_factory import (
    StartupOverrideGrantFactory
)
from accelerator.tests.factories.startup_program_interest_factory import (
    StartupProgramInterestFactory
)
from accelerator.tests.factories.startup_role_factory import StartupRoleFactory
from accelerator.tests.factories.startup_status_factory import (
    StartupStatusFactory
)
from accelerator.tests.factories.startup_team_member_factory import (
    StartupTeamMemberFactory
)
from accelerator.tests.factories.user_label_factory import UserLabelFactory
from accelerator.tests.factories.user_role_factory import UserRoleFactory
from accelerator.tests.factories.program_startup_attribute_factory import (
    ProgramStartupAttributeFactory
)
from accelerator.tests.factories.startup_attribute_factory import (
    StartupAttributeFactory
)

# Late Loading Factories
# These fail if put in alphabetical order in the above list
# presumably due to their SubFactorys.
from accelerator.tests.factories.expert_interest_factory import (
    ExpertInterestFactory
)
from accelerator.tests.factories.mentor_program_office_hour_factory import (
    MentorProgramOfficeHourFactory,
)
from accelerator.tests.factories.startup_mentor_relationship_factory import (
    StartupMentorRelationshipFactory,
)

# Other utility methods
from accelerator.tests.factories.factory_utils import expert_data
from simpleuser.tests.factories.user_factory import UserFactory
