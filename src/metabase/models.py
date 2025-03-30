from typing import Optional, Dict, Any

from pydantic import BaseModel


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