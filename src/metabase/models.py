from typing import  List, Optional, Dict, Any, Union
from pydantic import BaseModel

class LogEntry(BaseModel):
    timestamp: str
    level: str
    fqns: str
    msg: str
    exception: Optional[Any]
    process_uuid: str


class StatsExecution(BaseModel):
    executions: int
    by_status: Dict[str, Any]
    num_per_user: Dict[str, Any]
    num_by_latency: Dict[str, Any]

class StatsGroup(BaseModel):
    groups: int

class StatsTable(BaseModel):
    tables: int
    num_per_database: Dict[str, Any]
    num_per_schema: Dict[str, Any]

class StatsSystem(BaseModel):
    java_vm_specification_version: str
    java_runtime_name: str
    processors: int
    user_country: Optional[str]
    java_version: str
    user_language: str
    os_name: str
    user_timezone: str
    os_version: str
    file_encoding: str
    max_memory: int

class StatsQuestion(BaseModel):
    questions: Dict[str, int]
    public: Dict[str, Any]
    embedded: Dict[str, Any]

class StatsDashboard(BaseModel):
    dashboards: int
    with_params: int
    num_dashs_per_user: Dict[str, Any]
    num_cards_per_dash: Dict[str, Any]
    num_dashs_per_card: Dict[str, Any]
    public: Dict[str, Any]
    embedded: Dict[str, Any]

class StatsField(BaseModel):
    fields: int
    num_per_table: Dict[str, Any]

class StatsAlert(BaseModel):
    alerts: int
    with_table_cards: int
    first_time_only: int
    above_goal: int
    alert_types: Dict[str, Any]
    num_alerts_per_user: Dict[str, Any]
    num_alerts_per_card: Dict[str, Any]
    num_cards_per_alerts: Dict[str, Any]

class StatsCache(BaseModel):
    average_entry_size: int
    num_queries_cached: str
    num_queries_cached_unbinned: int

class StatsSegment(BaseModel):
    segments: int

class StatsPulse(BaseModel):
    pulses: int
    with_table_cards: int
    pulse_types: Dict[str, Any]
    pulse_schedules: Dict[str, Any]
    num_pulses_per_user: Dict[str, Any]
    num_pulses_per_card: Dict[str, Any]
    num_cards_per_pulses: Dict[str, Any]

class StatsDatabase(BaseModel):
    databases: Dict[str, int]
    dbms_versions: Dict[str, int]

class StatsCollection(BaseModel):
    collections: int
    cards_in_collections: int
    cards_not_in_collections: int
    num_cards_per_collection: Dict[str, Any]

class StatsUser(BaseModel):
    users: Dict[str, int]

class StatsMetric(BaseModel):
    metrics: int

class Stats(BaseModel):
    execution: StatsExecution
    group: StatsGroup
    table: StatsTable
    system: StatsSystem
    question: StatsQuestion
    dashboard: StatsDashboard
    field: StatsField
    alert: StatsAlert
    cache: StatsCache
    segment: StatsSegment
    pulse: StatsPulse
    database: StatsDatabase
    collection: StatsCollection
    user: StatsUser
    metric: StatsMetric

class UsageStats(BaseModel):
    appearance_no_object_illustration: str
    appearance_help_link: str
    embedding_app_origin_sdk_set: bool
    appearance_logo: bool
    appearance_landing_page_illustration: str
    appearance_login_page_illustration: str
    embedding_app_origin_interactive_set: str
    slack_configured: bool
    enable_embedding: bool
    report_timezone: str
    appearance_site_name: bool
    enable_embedding_sdk: bool
    running_on: str
    friendly_names: bool
    appearance_no_data_illustration: str
    check_for_updates: bool
    has_sample_data: bool
    appearance_favicon: bool
    application_database: str
    appearance_loading_message: bool
    email_configured: bool
    appearance_metabot_greeting: bool
    instance_started: str
    enable_embedding_interactive: bool
    sso_configured: bool
    appearance_show_mb_links: bool
    appearance_chart_colors: bool
    uuid: str
    startup_time_millis: int
    version: str
    timestamp: str
    embedding_app_origin_set: bool
    stats: Stats
    enable_embedding_static: bool
    appearance_ui_colors: bool

class Collection(BaseModel):
  authority_level: str
  description: str
  archived: bool
  slug: str
  archive_operation_id: str
  can_write: bool
  name: str
  personal_owner_id: str
  type: str
  can_restore: bool
  is_sample: bool
  effective_location: str
  parent_id: int
  id: int
  archived_directly: str
  entity_id: str
  location: str
  namespace: str
  is_personal: bool
  created_at: str
  can_delete: bool 
  effective_ancestors: list['Collection']

class SearchResults(BaseModel):

  description: str
  archived: bool
  collection_position: int
  table_id: int
  bookmark: bool
  can_write: bool
  database_id: int
  last_editor_common_name: str
  database_name: str
  pk_ref: str
  name: str
  type: str
  table_schema: str
  creator_common_name: str
  collection_authority_level: str
  creator_id: str
  updated_at: str
  moderated_status: str
  model_index_id: str
  model_id: str
  effective_location: str
  last_editor_id: str
  model_name: str
  id: int
  last_edited_at: str
  table_description: str
  dashboardcard_count: int
  context: str
  display: str
  scores: list['Scores']
  description: str
  initial_sync_status: str
  table_name: str
  location: str
  collection: dict
  created_at: str
  model: str

class Scores(BaseModel):
    weight: float
    score: float
    name: str
    column: str
    match: str

class TableMetaData(BaseModel):
  description: str | None = None
  entity_type: str | None = None
  view_count: int
  _schema: str | None = None
  database_require_filter: str | None = None
  db: 'TableDB'
  show_in_getting_started: bool
  name: str | None = None
  fields: List['TableFields']
  caveats: str | None = None
  segments: List[str]
  dimension_options: Union[List, Dict, None] = None
  updated_at: str | None = None
  active: bool
  id: int
  db_id: int
  entity_id: str | None = None
  visibility_type: str | None = None
  field_order: str | None = None
  is_upload: bool
  initial_sync_status: str | None = None
  display_name: str | None = None
  metrics: List
  created_at: str | None = None
  estimated_row_count: str | None = None
  points_of_interest: str | None = None

class TableDB(BaseModel):
    uploads_schema_name: str | None = None
    description: str | None = None
    features: List
    uploads_table_prefix: str | None = None
    cache_field_values_schedule: str | None = None
    timezone: str | None = None
    is_attached_dwh: bool
    auto_run_queries: bool
    metadata_sync_schedule: str | None = None
    name: str | None = None
    settings: str | None = None
    caveats: str | None = None
    creator_id: int
    is_full_sync: bool
    updated_at: str | None = None
    cache_ttl: str | None = None
    details: str | None = None
    is_sample: bool
    id: int
    is_on_demand: bool
    entity_id: str | None = None
    engine: str | None = None
    initial_sync_status: str | None = None
    is_audit: bool
    dbms_version: Dict[str, Any]
    uploads_enabled: bool
    refingerprint: str | None = None
    created_at: str | None = None
    points_of_interest: str | None = None

class TableFields(BaseModel):
      description: str | None = None
      database_type: str | None = None
      semantic_type: str | None = None
      table_id: int
      coercion_strategy: str | None = None
      database_indexed: str | None = None
      name: str | None = None
      fingerprint_version: int
      has_field_values: str | None = None
      settings: Dict[str, Any] | None = None
      caveats: str | None = None
      fk_target_field_id: str | None = None
      dimensions: List | None = None
      dimension_options: Union[List, Dict, None] = None
      updated_at: str | None = None
      custom_position: int
      effective_type: str | None = None
      active: bool
      nfc_path: str | None = None
      parent_id: str | None = None
      id: int
      last_analyzed: str | None = None
      database_partitioned: str | None = None
      database_is_auto_increment: bool
      json_unfolding: bool
      position: int
      entity_id: str | None = None
      visibility_type: str | None = None
      default_dimension_option: str | None = None
      target: str | None = None
      preview_display: bool
      display_name: str | None = None
      database_position: int
      database_required: bool
      name_field: str | None = None
      fingerprint: Dict[str, Any]
      created_at: str | None = None
      base_type: str | None = None
      points_of_interest: str | None = None

class MetricResultMetadata(BaseModel):
    display_name: str
    field_ref: List[Union[str, int]]
    base_type: str
    effective_type: str
    database_type: str
    name: str
    semantic_type: str
    fingerprint: Dict[str, Any]

class MetricAggregationOptions(BaseModel):
    name: str
    display_name: str

    class Config:
        flds = {'display_name': 'display-name'}

class MetricQuery(BaseModel):
    source_table: int
    aggregation: List[Union[List[Any], Dict[str, Any]]]

    class Config:
        flds = {
            'source_table': 'source-table',         
        }

class MetricDatasetQuery(BaseModel):
    database: int
    type: str
    query: MetricQuery

class MetricCard(BaseModel):
    name: str
    type: str
    dataset_query: MetricDatasetQuery
    display: str
    description: Optional[str]
    visualization_settings: Dict[str, Any]
    collection_position: int
    result_metadata: List[MetricResultMetadata]
    collection_id: int
